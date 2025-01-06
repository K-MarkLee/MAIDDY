from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'birth_of_date', 'bio', 'gender', 'profile_image']
        extra_kwargs = {
            'password': {'write_only': True},  # 비밀번호는 출력하지 않음, just 읽기전용
        }
    


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

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'birth_of_date', 'bio', 'profile_image','gender']