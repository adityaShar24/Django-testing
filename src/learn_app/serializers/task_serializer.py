from rest_framework import serializers
from ..models.task_model import Task
from django.core.validators import RegexValidator

class TaskSerializer(serializers.ModelSerializer):
    
    title = serializers.CharField(validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Only letters are allowed.', code='invalid_title')])
    class Meta:
        
        model = Task
        
        fields = ['id', 'title', 'is_completed', 'date', 'user']