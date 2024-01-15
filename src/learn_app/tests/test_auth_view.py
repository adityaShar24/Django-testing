from .test_setup import TestSetUp

class TestRegisterViews(TestSetUp):
    
    def test_register(self):
        self.create_test_user()  
        response = self.client.post(self.register_url , self.user_data, format='json')
        
        self.assertEqual(response.status_code , 201)

    def test_register_invalid_data(self):
        
        invalid_user_data = {
            'username': 123,
            "password": 'viswa'
        }
        response = self.client.post(self.register_url , invalid_user_data , format='json')
        self.assertEqual(response.status_code , 400)
        


class TestLoginView(TestSetUp):
    
    def test_login_with_no_data(self):
        
        response = self.client.post(self.login_url, {}, format='json')

        self.assertEqual(response.status_code, 400)
            
    def test_login_with_data(self):
        self.create_test_user()
        login_data = {
            'username': 'username_02',
            'password': 'paxa'
        }
        response = self.client.post(self.login_url , login_data , format='json')

        self.assertEqual(response.status_code , 201)
        self.assertIn('access', response.data)
    
class TestListUsers(TestSetUp):
    
    def test_list_success(self):
        
        
        response = self.client.get(
            self.list_url , 
            format='json', 
            HTTP_AUTHORIZATION = f'Bearer {self.access_token}'
        )
        
        self.assertEqual(response.status_code , 200)
