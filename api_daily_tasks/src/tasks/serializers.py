from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from .models import Task

from rest_framework.validators import UniqueValidator
from rest_framework import serializers

#from rest_framework_jwt.settings import api_settings

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'