from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'is_staff',
            'is_active', 'date_joined')

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)