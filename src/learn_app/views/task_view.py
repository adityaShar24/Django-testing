from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from ..serializers.task_serializer import TaskSerializer
from ..models.task_model import Task
from ..utils.constants import PERMISSION_DENIED_MESSAGE , TASK_UPDATED_MESSAGE
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

class UpdateTaskView(APIView):
    def post(self , request , pk):
        
        response = None
        task = Task.objects.get(id = pk)
        
        if task.user.id != request.user.id:
            response_data = {
                "message": PERMISSION_DENIED_MESSAGE
            }

            response = Response(response_data , HTTP_201_CREATED)
        else:
            data = {
                'title': request.data.get('title'),
                'user': request.user.id
            }
            
            serializer = TaskSerializer(data= data)
            
            if serializer.is_valid():
                serializer.save()
                
                resposne_data = {
                    'message': TASK_UPDATED_MESSAGE,
                    'data': serializer.data
                }
                
                response = Response(resposne_data , HTTP_201_CREATED)
                
            else:
                response = Response(serializer.errors , HTTP_400_BAD_REQUEST)
        
        return response
        
