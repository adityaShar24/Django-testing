from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.list_url = reverse('list')
        
        self.create_task_url = reverse('create')
        
        self.task_data = {
            'title': 'Learn CBV in django',
            'user': 2
        }

        self.user_data = {
            'username': 'krisna',
            'password': 'viswa'
        }

        super().setUp()

    def create_test_user(self, username='username_02', password='paxa'):
        return User.objects.create_user(username=username, password=password)