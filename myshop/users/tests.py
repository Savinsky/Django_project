from django.test import TestCase
from django.contrib.auth.models import User, Group
# Create your tests here.
class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {'username': 'testuser', 'password':'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    #user = mixer.blend(User, username='testuser', groups__name='admin')
