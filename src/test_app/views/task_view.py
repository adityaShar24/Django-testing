from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , HTTP_403_FORBIDDEN , HTTP_200_OK  , HTTP_404_NOT_FOUND
from ..serializers.task_serializer import TaskSerializer
from ..models.task_model import Task
from ..utils.constants import PERMISSION_DENIED_MESSAGE , TASK_UPDATED_MESSAGE
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [JWTAuthentication]   
    def post(self , request):
        try:
            response = None
            
            data = {
                'title': request.data.get('title'),
                'user': request.user.id
            }
            
            serializer = TaskSerializer(data= data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            resposne_data = {
                'message': 'Task has been created successfully!',
                'data': serializer.data
            }
            
            response = Response(resposne_data , HTTP_201_CREATED)
        
        except Exception as e:
            response = Response({'error': str(e)} , HTTP_400_BAD_REQUEST) 
        
        return response 
class UpdateTaskView(APIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [JWTAuthentication] 
    
    def put(self , request , pk):
        try:
            response = None
            task = Task.objects.get(id = pk)
            
            if task.user.id != request.user.id:
                raise PermissionError(PERMISSION_DENIED_MESSAGE)
            
            data = {
                'title': request.data.get('title' , task.title),
                'is_completed': request.data.get('is_completed' , task.is_completed),
                'user': request.user.id
            }
            
            serializer = TaskSerializer(task , data= data , partial = True)
            
            serializer.is_valid(raise_exception=True)
            serializer.save()
                
            resposne_data = {
                    'message': TASK_UPDATED_MESSAGE,
                    'data': serializer.data
            }
                
            response = Response(resposne_data , HTTP_200_OK)
            
        except PermissionError as e:
            response = Response({'error': str(e)}, HTTP_403_FORBIDDEN)

        except Task.DoesNotExist:
            response = Response({'error': 'Task not found'}, HTTP_404_NOT_FOUND)

        except Exception as e:
            response = Response({'error': str(e)}, HTTP_400_BAD_REQUEST)

        return response

class ListTaskView(APIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [JWTAuthentication]  
    
    def get(self , request):
        
        response = None
        tasks = Task.objects.all()
        
        serializer = TaskSerializer(instance= tasks , many=True)
        

        respone_data = {
                'message': 'fetched all tasks successfully!',
                'tasks': serializer.data
            }
            
        response = Response(respone_data , HTTP_200_OK)
        
        return response
    
class GetDetailTaskView(APIView):
    permission_classes = [IsAuthenticated]    
    authentication_classes = [JWTAuthentication]  
    
    def get(self , request):
        response = None
        
        pk = self.request.query_params.get('id')
        
        if pk is None:
            response_data = {
                "message": "pk is required!",
            }

            response = Response(response_data , HTTP_400_BAD_REQUEST)
            
        
        task = Task.objects.get(id = pk )
        
        if task.user.id != request.user.id:
            response_data = {
                "message": PERMISSION_DENIED_MESSAGE,
            }

            response = Response(response_data , HTTP_403_FORBIDDEN)
        else:
            serializer = TaskSerializer(instance= task)
            
            respone_data = {
                    'message': 'fetched task successfully!',
                    'task': serializer.data
                }
                
            response = Response(respone_data , HTTP_200_OK)
        
        return response