from .test_setup import TestSetUp
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class CreateTaskViewTest(TestSetUp):
    
    def test_create_task_with_no_data(self):
        response = self.client.post(self.create_task_url)
        self.assertEqual(response.status_code , 400)
    
    def test_create_task_with_data(self):
        response = self.client.post(
            self.create_task_url,
            self.task_data,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        
        self.assertEqual(response.status_code, 201, f"Response data: {response.data}")
    
    
    def test_create_task_with_invalid_data(self):
        
        invalid_task_data = {
            'username': 123,
            "password": 'viswa'
        }
        
        response = self.client.post(
            self.create_task_url,
            invalid_task_data,
            format= 'json'
        )
        
        self.assertEqual(response.status_code , 400)
        

class UpdateTaskViewTest(TestSetUp):
    
    def test_update_task_success(self):
        data = {'title': 'Updated Task Title'}
        
        response = self.client.post(
            self.update_task_url , 
            data , 
            format='json' , 
            HTTP_AUTHORIZATION = f'Bearer {self.access_token}'
        )
        
        self.assertEqual(response.status_code , 201)

    def test_update_permission_denied(self):
        
        another_user = self.create_test_user(username='another_user1' , password='password22')
        another_user_token = str(AccessToken.for_user(another_user))
        
        data = {'title': 'Attempted Update'}
        
        response = self.client.post(
            self.update_task_url,
            data,
            format='json',
            HTTP_AUTHORIZATION = f'Bearer {another_user_token}'
        )
        
        self.assertEqual(response.status_code, 403)
        