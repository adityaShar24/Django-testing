from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from ..utils.constants import USER_REGISTERED_MESSAGE
from ..serializers.user_serializer import RegisterSerializer
from ..serializers.login_serializer import LoginSerializer


class RegisterView(APIView):
    
    def post(self , request):
        
        response = None
        
        data = request.data
        
        serializer = RegisterSerializer(data = data)
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
        
            reponse_data = {
                "message": USER_REGISTERED_MESSAGE,
                "data": serializer.data
            }
            
            response = Response(reponse_data , HTTP_201_CREATED)
        else:
            response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST) 
    
        return response

        