from django.urls import path
from ..views.task_view import CreateTaskView , UpdateTaskView

urlpatterns = [
    path('create' , CreateTaskView.as_view() , name='create'),
    path('update/<str:pk>' , UpdateTaskView.as_view() , name='update'),
]
