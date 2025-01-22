from rest_framework import status
from .serializers import UserCreateSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes



User = get_user_model()


# 회원가입 API
@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([AllowAny])      # 권한 비활성화
def user_create(request):
    try:
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": f"{serializer.data['username']}님 회원가입이 정상적으로 완료되었습니다.",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



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
