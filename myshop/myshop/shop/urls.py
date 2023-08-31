"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myshop.shop import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
    path('', views.MainPage.as_view(), name = 'home'),
    path('product/<slug:product_slug>/', views.ShowProduct.as_view(), name = 'product'),
    path('shop/', views.ShopPage.as_view(), name = 'shop'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('addproduct/', views.AddProduct.as_view(), name='add_product'),
    path('category/<slug:cat_slug>/', views.ProductCategory.as_view(), name='category'),
    #path('cart/', views),

    path('category-one/<int:pk>', views.CategoryDetailView.as_view(), name='category_one'),
    #path('category-update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    #path('category-delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
    #path('category-create/', views.CategoryCreateView.as_view(), name='category_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)