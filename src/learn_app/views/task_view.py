from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from ..serializers.task_serializer import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateTaskView(APIView):
    
    authentication_classes = [JWTAuthentication]   
    def post(self , request):
    
        response = None
        
        data = {
            'title': request.data.get('title'),
            'user': request.user.id
        }
        
        serializer = TaskSerializer(data= data)
        
        
        if serializer.is_valid():
            serializer.save()
            
            resposne_data = {
                'message': 'Task has been created successfully!',
                'data': serializer.data
            }
            
            response = Response(resposne_data , HTTP_201_CREATED)
        
        else:
            response = Response(serializer.errors , HTTP_400_BAD_REQUEST)
        
        return response
