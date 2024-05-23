from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json

from api.serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


User = get_user_model()

@csrf_exempt
def signup(request):    
    if request.method == "POST":
        fbody_unicode = request.body.decode('utf-8')
        body_data = json.loads(fbody_unicode)
        email = body_data.get('email')
        password = body_data.get('password')
        first_name = body_data.get('first_name', '')
        last_name = body_data.get('last_name', '')

        # 데이터베이스에 사용자 생성
        user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name)

        return JsonResponse({'message': 'User created successfully'})
    
    return JsonResponse({'hello': 'world'})

        
@csrf_exempt
def login(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        email = body_data.get('email')
        password = body_data.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # 사용자 인증이 성공한 경우 토큰 생성
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "로그인 성공", "token": token.key})
        else:
            # 사용자 인증이 실패한 경우
            return JsonResponse({"message": "로그인 실패"}, status=401)
    return JsonResponse({"message": "확인 성공"})



class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user == user or request.user.is_superuser:
            self.perform_destroy(user)
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You do not have permission to delete this user.'}, status=status.HTTP_403_FORBIDDEN)