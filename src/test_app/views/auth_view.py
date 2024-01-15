from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , HTTP_200_OK 
from rest_framework_simplejwt.tokens import AccessToken , RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..utils.constants import USER_REGISTERED_MESSAGE , INVAID_CREDENTIALS_MESSAGE , USER_LOGGEDIN_MESSAGE , ALL_USERS_FETCHED_MESSAGE
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
        
            response_data = {
                "message": USER_REGISTERED_MESSAGE,
                "data": serializer.data
            }
            
            response = Response(response_data , HTTP_201_CREATED)
        else:
            response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST) 
    
        return response


class LoginView(APIView):
    
    def post(self , request):
        
        response = None
        
        data = request.data
        
        serializer = LoginSerializer(data = data)

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            
            user = authenticate(request = request , username = username , password = password)
            
            
            if user is None:
                response = Response({"message": INVAID_CREDENTIALS_MESSAGE} , HTTP_400_BAD_REQUEST)
            
            access = AccessToken.for_user(user)
            
            
            refresh = RefreshToken.for_user(user)
            
            response_data = {
                    "message": USER_LOGGEDIN_MESSAGE.format(username = username), 
                    "refresh": str(refresh),
                    "access": str(access)
                }
            
            
            response = Response( response_data , status= HTTP_201_CREATED)
            
        else:
            response = Response(serializer.errors , HTTP_400_BAD_REQUEST)
            
        return response



class ListUsersView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]   

    
    def get(self , request):
        
        response = None
        
        users = User.objects.all()
        
        serializer = RegisterSerializer(users , many = True)
        
        response_data = {
            "message": ALL_USERS_FETCHED_MESSAGE,
            "data": serializer.data
        }
        
        response = Response(response_data , status= HTTP_200_OK)
        
        return response