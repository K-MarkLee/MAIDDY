from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


User = get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators =[validate_password]) # 비밀번호 입력 필드
    password2 = serializers.CharField(write_only=True, required=True) # 비밀번호 확인 필드

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2'] #MVP용
    

    def validate(self, data): # 회원가입시 비밀번호 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': '비밀번호가 일치하지 않습니다.'})
        return data
    

    def create(self, validated_data):
        validated_data.pop('password2') # password2 필드 삭제
        return User.objects.create_user(**validated_data)

