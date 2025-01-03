from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes

User = get_user_model()


# Create your views here.
@api_view(['POST']) # POST 요청만 받음
@permission_classes([])
@authentication_classes([])

def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "회원가입이 완료되었습니다!"}, status=status.HTTP_201_CREATED)
    return render(serializer.errors, status=status.HTTP_400_BAD_REQUEST)