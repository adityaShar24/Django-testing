from .test_setup import TestSetUp
import pdb

class TestViews(TestSetUp):
    
    def test_register_with_no_data(self):
        
        response = self.client.post(self.register_url)
        
        self.assertEqual(response.status_code , 400)
        
    def test_register(self):
        self.create_test_user()  
        response = self.client.post(self.register_url , self.user_data, format='json')
        
        self.assertEqual(response.status_code , 201)

    def test_login_with_no_data(self):
        
        response = self.client.post(self.login_url, {}, format='json')

        self.assertEqual(response.status_code, 400)
            
    def test_login(self):
        user = self.create_test_user()  # Create a new user for this test
        login_data = {
            'username': 'user',
            'password': 'users_password',
        }
        response = self.client.post(self.login_url , login_data , format='json')
        self.assertEqual(response.status_code , 201)