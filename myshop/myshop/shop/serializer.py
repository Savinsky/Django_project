from django.urls import path, include
from .models import Product, Category
from rest_framework import routers, serializers, viewsets

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ['image', 'created', 'updated']
        #fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'