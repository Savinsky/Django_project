from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.utils.functional import cached_property

from .models import Category, Product
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterUserForm, AddProductForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class MainPage(DataMixin, ListView):
    model = Product
    template_name = 'myshop/index.html'
    context_object_name = 'prods'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= "Главная страница интернет-магазина")
        context = dict(list(context.items()) + list(c_def.items()))

        list_product = Product.active_objects.all().prefetch_related('product_cat').only('name', 'price', 'image')
        paginator = Paginator(list_product, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context['list_product'] = products

        return context

    def get_queryset(self):
        return Product.objects.filter(available = True)

class ShopPage(ListView):
    model = Product
    template_name = 'myshop/shop.html'
class CartPage(DetailView):
    #model =
    template_name = 'myshop/cart.html'
class CheckoutPage(FormView):
    template_name = 'myshop/checkout.html'
class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'myshop/single-product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['products'])
        return dict(list(context.items()) + list(c_def.items()))
    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        return object

class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'myshop/product_add.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    #raise_exception = True #запрет доступа к странице либо декоратор для функции @login_required

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление товара')
        return dict(list(context.items()) + list(c_def.items()))

class ProductCategory(DataMixin, ListView):
    model = Category
    template_name = 'myshop/index.html'
    context_object_name = 'prods'
    allow_empty = False
    def get_queryset(self):
        return Product.objects.filter(cat__clug=self.kwargs['cat_slug'], is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['products'][0].cat),
                                      cat_selected=context['products'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'myshop/single-product.html'

class CategoryUpdateView(UpdateView):
    template_name = 'myshop/category_update.html'
    model = Category
    success_url = reverse_lazy('myshop:category_list')

'''
class CategoryDeleteView(DeleteView):
    template_name = 'myshop/category_delete.html'
    model = Category
    success_url = reverse_lazy('myshop:category_list')

class CategoryCreateView(CreateView):
    fields = '__all__'
    template_name = 'myshop/category_create.html'
    model = Category
    success_url = reverse_lazy('myshop:category_list') 
'''

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'myshop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'myshop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class PermissionMixin:
    def test_func(self):
        return self.request.user.is_superuser
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('shop:index'))

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'myshop/single-product.html', {'product': product,
                                                          'cart_product_form': cart_product_form})
