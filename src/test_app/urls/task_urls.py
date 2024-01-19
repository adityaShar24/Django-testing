from django.urls import path
from ..views.task_view import CreateTaskView , UpdateTaskView , ListTaskView , GetDetailTaskView

urlpatterns = [
    path('create' , CreateTaskView.as_view() , name='create'),
    path('update/<str:pk>' , UpdateTaskView.as_view() , name='update'),
    path('list' , ListTaskView.as_view() , name='list'),
    path('detail' , GetDetailTaskView.as_view() , name='detail'),
]
