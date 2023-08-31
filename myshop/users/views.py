from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .models import ShopUser
from .forms import RegisterUserForm

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('myshop|index')