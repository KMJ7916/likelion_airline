from rest_framework import serializers
from .models import User
import json

def serialize_signup(user):
    return{
        "firstName":user.firstName,
        "lastName":user.lastName,
        "email":user.email,
        'password':user.password,
    }
    
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드는 쓰기 전용으로 설정