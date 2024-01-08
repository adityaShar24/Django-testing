from .test_setup import TestSetUp
import pdb

class TestViews(TestSetUp):
    
    def test_register_with_no_data(self):
        
        response = self.client.post(self.register_url)
        
        self.assertEqual(response.status_code , 400)
        
    def test_register(self):
        
        response = self.client.post(self.register_url , self.user_data, format='json')
        self.assertEqual(response.status_code , 201)
