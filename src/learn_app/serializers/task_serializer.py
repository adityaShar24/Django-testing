from rest_framework import serializers
from ..models.task_model import Task


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Task
        
        fields = ['id', 'title', 'is_completed', 'date', 'user']