from django.urls import path
from ..views.auth_view import RegisterView , LoginView , ListUsersView


urlpatterns = [
    path('register' , RegisterView.as_view() , name='register'),
    path('login' , LoginView.as_view() , name='login'),
    path('list' , ListUsersView.as_view() , name='list'),
]
