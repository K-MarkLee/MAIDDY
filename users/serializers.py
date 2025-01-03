from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password]) #검증 
    password2 = serializers.CharField(write_only=True, requried=True) # 확인이라서 검증 필요없음

    class Meta:
        model = User # User모델
        fields = ['email', 'username', '']