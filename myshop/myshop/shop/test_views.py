from django.test import Client
from django.test import TestCase

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_status_login_page(self):
        response = self.client.post('/login/', {'username': 'admin', 'password': 'qwerty'})
        print(response.status_code)
        #self.assertEqual(response.status_code, 404)


class TestProfileImageUploadForm(TestCase):
    pass
