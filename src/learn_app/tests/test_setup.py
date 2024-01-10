from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'username': 'krisna',
            'password': 'viswa'
        }

        super().setUp()

    def create_test_user(self, username='jayshreeVuva', password='Vuva'):
        return User.objects.create_user(username=username, password=password)