from django.core.management.base import BaseCommand
from myshop.myshop.shop.models import Product, Category
from mixer.backend.django import mixer

class Command(BaseCommand):
    def handle(self, *args, **options):
        product = mixer.cycle(100).blend(Product)