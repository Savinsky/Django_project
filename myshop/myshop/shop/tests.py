from django.test import TestCase
#from faker import Faker
from mixer.backend.django import mixer
from models import Category, Product

# Create your tests here.

class ShopTestCase(TestCase):
    def SetUp(self):
        cat1 = mixer.blend(Category, cat_name = 'Смартфоны')
        cat2 = mixer.blend(Category, cat_name = mixer.random)
        self.product = mixer.blend(Product, product_name = mixer.fake)
        self.product.product_cat.add(cat1, cat2)
        print(cat1.cat_name, cat2.cat_name)
        print(self.product.product_name, self.product.product_text)

    def test_how_many(self):
        self.assertEqual(self.product.cat_number(), 2)

    def test_is_one(self):
        self.assertFalse(self.product.is_cat_one())

    def test_create_category(db):
        category = Category.objects.create(name='Books')
        assert category.name == "Books"

    def test_product_one(product_one):
        assert product_one.name == "Book 1"
        assert product_one.is_available

    def test_name_product_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        self.assertEquals(product.get_absolute_url(), '/prods/1')