from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth import authenticate

# Create your views here.


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
    firstname= request.POST['firstName']
    return JsonResponse({"message": "확인 성공"})



@csrf_exempt
def delete_account(request):    
    if request.method == "POST":
        # 필요한 데이터를 요청에서 가져옵니다.
        user_id = request.POST.get('user_id')  # 예시: 요청에 사용자 ID를 담아서 전달받음

        # 사용자를 데이터베이스에서 찾습니다.
        try:
            user = User.objects.get(id=user_id)
            # 사용자를 삭제합니다.
            user.delete()
            return JsonResponse({"message": "회원 탈퇴가 성공적으로 처리되었습니다."})
        except User.DoesNotExist:
            return JsonResponse({"error": "해당 사용자가 존재하지 않습니다."}, status=404)

    # POST 요청이 아닌 경우, 예외 처리
    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)