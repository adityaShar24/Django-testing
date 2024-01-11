from django.urls import path
from ..views.task_view import CreateTaskView

urlpatterns = [
    path('create' , CreateTaskView.as_view() , name='create'),
]
