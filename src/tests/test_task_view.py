from .test_setup import TestSetUp

class TaskTestViews(TestSetUp):
    
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
                
        self.assertEqual(response.status_code, 201)