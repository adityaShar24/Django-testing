from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Only letters are allowed.', code='invalid_username')])
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id' , 'username', 'password')
        