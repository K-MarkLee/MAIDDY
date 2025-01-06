from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.forms import SetPasswordForm
import logging



User = get_user_model()


# 회원가입 API
@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([])      # 권한 비활성화
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User created successfully",
            "user": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 로그인 API

@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([])      # 권한 비활성화
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # 사용자 인증
    user = authenticate(request, username=username, password=password)

    if user is not None: 
        # 인증 성공: 토큰 발급(JWT 토큰 생성)
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "message": "Login successful",
        }, status=status.HTTP_200_OK)
    else:
        # 인증 실패
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST']) # POST 요청만 허용
def logout(request):
    try:
        refresh_token = request.data.get('refresh') # refresh 토큰 가져오기 (refresh 토큰이란 access 토큰을 재발급하는 토큰)
        
        token = RefreshToken(refresh_token) # refresh 토큰 생성
        token.blacklist() # 토큰 블랙리스트 추가 (토큰 만료로 로그아웃 처리)

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    
    except:
        refresh_token = request.data.get('refresh')
        print(refresh_token)
        return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET']) # GET 요청만 허용
def profile(request, username):
    if request.method == 'GET': # GET 요청인 경우 프로필 조회
        user = get_object_or_404(User, username=username)   
        try:
            serializer = ProfileSerializer(user)

        except User.DoesNotExist: # 사용자가 존재하지 않는 경우
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK) 

# 수정은 프로필 칸 들어가서!!!!! 여기서는 조회만!!!






# 비밀번호 재설정 요청 API (이메일로 링크 보내기)
@api_view(['POST'])
@authentication_classes([])  # 인증 비활성화
@permission_classes([])  # 권한 비활성화
def password_reset_request(request):
    email = request.data.get('email')
    user = get_object_or_404(User, email=email)

    # 사용자에게 비밀번호 재설정 이메일 발송
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(user.pk.encode())
    
    reset_url = f"http://{get_current_site(request).domain}{reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})}"
    subject = "Password Reset Request"
    message = render_to_string('password_reset_email.html', {
        'user': user,
        'reset_url': reset_url
    })
    
    send_mail(subject, message, 'noreply@example.com', [email])

    return Response({
        "message": "Password reset email sent"
    }, status=status.HTTP_200_OK)


# 비밀번호 재설정 확인 및 새 비밀번호 설정 API
@api_view(['POST'])
def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        
        if default_token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            form = SetPasswordForm(user, data={'new_password1': new_password, 'new_password2': new_password})
            
            if form.is_valid():
                form.save()
                return Response({
                    "message": "Password has been reset successfully."
                }, status=status.HTTP_200_OK)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logging.error(f"Error during password reset: {e}")
        return Response({"error": "Invalid token or user"}, status=status.HTTP_400_BAD_REQUEST)
