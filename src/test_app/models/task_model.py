from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    title = models.CharField(max_length=255)
    
    is_completed = models.BooleanField(default=False)
    
    date = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE , related_names = 'tasks')

    def __str__(self):
        return self.title
