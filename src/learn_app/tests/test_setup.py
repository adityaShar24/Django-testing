from rest_framework.test import APITestCase
from django.urls import reverse



class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        
        
        self.user_data = {
            'username': 'user',
            'password':'users_password',
            'email': 'user@email.com'
        }
        
        return super().setUp()