from rest_framework import status
from .serializers import UserCreateSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProfileSerializer



User = get_user_model()


# 회원가입 API
@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([AllowAny])      # 권한 비활성화
def user_create(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": f"{serializer.data['username']}님 회원가입이 정상적으로 완료되었습니다.",
            "user": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 로그인 API
@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([AllowAny])      # 권한 비활성화
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # 사용자 인증
    user = authenticate(request, email=email, password=password)

    if user is not None: 
        # 인증 성공: 토큰 발급(JWT 토큰 생성)
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "message": f"{user.username}님, 반갑습니다!",
        }, status=status.HTTP_200_OK)
    else:
        # 인증 실패
        return Response({"error": "로그인 정보가 올바르지 않습니다. 다시한번 확인해주세요."}, status=status.HTTP_401_UNAUTHORIZED)



# 로그아웃 API
@api_view(['POST'])
@authentication_classes([])  # JWT 인증 비활성화
@permission_classes([AllowAny])  # 권한 비활성화
def logout(request):
    try:
        refresh_token = request.data.get('refresh')  # refresh token을 body에서 가져오기

        if not refresh_token:
            return Response({"error": "refresh token이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)  # refresh 토큰 생성
        token.blacklist()  # 토큰 블랙리스트 추가 (블랙리스트 : 토큰 만료되면 로그아웃됨)

        return Response({"message": "로그아웃되었습니다."}, status=status.HTTP_200_OK)
    
    except Exception as logout_failure:
        return Response({"error": "로그아웃에 실패하셨습니다.", "details": str(logout_failure)}, status=status.HTTP_400_BAD_REQUEST)





# 프로필 조회 API
@api_view(['GET'])
@authentication_classes([JWTAuthentication])  # JWT 인증 활성화
def user_profile(request):
    user = request.user
    serializer = ProfileSerializer(user)  # ProfileSerializer로 모든 필드를 직렬화

    return Response(serializer.data, status=status.HTTP_200_OK)



# 프로필 수정 API
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])  # JWT 인증 활성화
def update_profile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)  # 일부 필드만 수정 가능

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": f"{user.username}님의 프로필이 수정되었습니다.",
            "user": serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 비밀번호 변경 API
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])  # JWT 인증 활성화
def change_password(request):
    user = request.user
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')

    if not user.check_password(current_password):
        return Response({"error": "현재 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    user.password = make_password(new_password)  # 새 비밀번호 암호화
    user.save()
    return Response({"message": "비밀번호가 변경되었습니다."}, status=status.HTTP_200_OK)

# 회원 탈퇴 API
@api_view(['DELETE'])
def delete_account(request):
    user = request.user
    user.delete()  # 사용자 삭제
    return Response({"message": "회원탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)

