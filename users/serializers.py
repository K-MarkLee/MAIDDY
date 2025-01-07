from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


User = get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators =[validate_password]) # 비밀번호 입력 필드
    password2 = serializers.CharField(write_only=True, required=True) # 비밀번호 확인 필드

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'birth_of_date', 'bio', 'gender', 'profile_image']
    

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            gender=validated_data.get('gender'),
            bio=validated_data.get('bio'),
            birth_of_date=validated_data.get('birth_of_date')
        )
        return user


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'birth_of_date', 'bio', 'profile_image','gender']