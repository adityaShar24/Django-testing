from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse
from django.contrib.auth.models import User
from ..models.task_model import Task

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.list_url = reverse('list')
        
        self.user = self.create_test_user(username='anotheruser', password='anotheruseris')
        self.access_token = str(AccessToken.for_user(self.user))
        
        self.create_task_url = reverse('create')
        
        
        self.task = Task.objects.create(title= 'Test Task' , user = self.user)
        
        self.update_task_url = reverse('update' ,  kwargs={'pk': self.task.id})
        self.list_tasks_url = reverse('list')

        
        self.task_data = {
            'title': "Learn CBV in django",
            'user': self.user.id
        }

        self.user_data = {
            'username': 'kisna',
            'password': 'viswa'
        }

        super().setUp()

    def create_test_user(self, username='username_02', password='paxa'):
        return User.objects.create_user(username=username, password=password)