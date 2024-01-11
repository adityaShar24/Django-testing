from .test_setup import TestSetUp

class TaskTestViews(TestSetUp):
    
    def test_create_task_with_no_data(self):
        
        response = self.client.post(self.create_task_url)
        
        self.assertEqual(response.status_code , 400)
    
    def test_create_task_with_data(self):
            # Ensure that the `setUp` method from `TestSetUp` is called first
            self.setUp()

            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_access_token()}')
                
            response = self.client.post(self.create_task_url, self.task_data, format='json')
            print(response.data)
            
            self.assertEqual(response.status_code, 201)

    def get_access_token(self):
        # Use the JWT library or your authentication method to get a valid access token
        # Here's a simple example using the django-rest-framework-simplejwt library
        from rest_framework_simplejwt.tokens import AccessToken

        token = AccessToken.for_user(self.user)
        return str(token)