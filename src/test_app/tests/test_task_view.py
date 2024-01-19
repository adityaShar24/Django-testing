from .test_setup import TestSetUp
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse

class CreateTaskViewTest(TestSetUp):

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
            format= 'json',
            HTTP_AUTHORIZATION = f'Bearer {self.access_token}'
        )
        
        self.assertEqual(response.status_code , 400)
        

class UpdateTaskViewTest(TestSetUp):
    
    def test_update_task_success(self):
        data = {'title': 'Updated Task Title' , 'is_completed': True}
        
        response = self.client.put(
            self.update_task_url , 
            data , 
            format='json' , 
            HTTP_AUTHORIZATION = f'Bearer {self.access_token}'
        )
        
        self.assertEqual(response.status_code , 200)

    def test_update_permission_denied(self):
        
        another_user = self.create_test_user(username='another_user1' , password='password22')
        another_user_token = str(AccessToken.for_user(another_user))
        
        data = {'title': 'Attempted Update'}
        
        response = self.client.put(
            self.update_task_url,
            data,
            format='json',
            HTTP_AUTHORIZATION = f'Bearer {another_user_token}'
        )
        self.assertEqual(response.status_code, 403)
        
class ListTaskViewTest(TestSetUp):
    
    def test_list_tasks_success(self):
        response = self.client.get(
            self.list_tasks_url,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'fetched all tasks successfully!')
        self.assertIn('tasks', response.data)
        
        self.assertIsInstance(response.data['tasks'], list)
        self.assertTrue(all('title' in task for task in response.data['tasks']))
        
    def task_list_permission_denied(self):
        
        another_user = self.create_test_user(username='another_user1' , password='password22')
        another_user_token = str(AccessToken.for_user(another_user))
        
        response = self.client.get(
            self.list_tasks_url,
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {another_user_token}'
        )
        
        self.assertEqual(response.status_code, 403)
    
# class GetDetailTaskViewTest(TestSetUp):
    
#     get_detail_task_url = reverse('detail' , kwargs={'id': 1})
    
#     def test_get_detail_task_success(self):
#         response = self.client.get(
#             self.get_detail_task_url,
#             format='json',
#             HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
#         )
#         print(response.data)
#         self.assertEqual(response.status_code, 200)
        
#     def test_get_detail_task_permission_denied(self):
        
#         another_user = self.create_test_user(username='another_user1' , password='password22')
#         another_user_token = str(AccessToken.for_user(another_user))
        
#         response = self.client.get(
#             self.get_detail_task_url,
#             format='json',
#             HTTP_AUTHORIZATION=f'Bearer {another_user_token}'
#         )
        
#         self.assertEqual(response.status_code, 403)