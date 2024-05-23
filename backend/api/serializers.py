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