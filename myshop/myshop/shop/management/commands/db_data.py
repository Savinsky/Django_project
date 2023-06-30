from django.core.management.base import BaseCommand
from myshop.shop.models import Category, Product
"""
class Command(BaseCommand):

    def handle(self, *args, **options):

        products = Product.objects.all()
        print(type(products), products)
        for prod in products:
            print(prod.name)

        prod_ = Product.objects.get(name = 'sport')
        print(prod_)

        #categ = Category.objects.filter(name = 'sport')
        #print(categ)

        print(prod_.Category.all())
        print(prod_.Category.first())

        Category.objects.create(name = 'Ноутбуки')
        categs = Category.objects.all()
        print(categs)

        cat = Category.objects.filter(name = 'Ноутбуки')
        cat.delete()
        categs = Category.objects.all()
        print(categs)
"""


