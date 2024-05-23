from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ObtainToken(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': '인증 실패'}, status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
def signup(request):    
    if request.method=="POST":
        fbody_unicode = request.body.decode('utf-8')
            # JSON 문자열을 파이썬 딕셔너리로 파싱
        body_data = json.loads(fbody_unicode)
        email = body_data.get('email')
        password = body_data.get('password')
        first_name = body_data.get('firstName', '')
        last_name = body_data.get('lastName', '')

        # 데이터베이스에 저장
        user = User.objects.create(email=email, password=password, firstName=first_name, lastNam=last_name)
        
        return JsonResponse({"message": "회원가입 성공"})
    
    return JsonResponse({'hello':'world'})

@csrf_exempt
def login(request):
    if request.method=="POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        email = body_data.get('email')
        password = body_data.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        return JsonResponse({"message": "로그인 성공"})
    return JsonResponse({"message": "로그인 성공"})


@csrf_exempt
def delete_user(request,):
    if request.method=="POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        email = body_data.get('email')
        password = body_data.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        return JsonResponse({"message": "User deleted successfully"})
    return JsonResponse({"message": "User deleted successfully"})


class DeleteAccount(APIView):
    permission_classes = [IsAuthenticated]

    def delete(request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": "회원 탈퇴가 성공적으로 처리되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "해당 사용자가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)