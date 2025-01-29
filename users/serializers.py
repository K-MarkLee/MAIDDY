from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


User = get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators =[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
    

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': '비밀번호가 일치하지 않습니다.'})
        return data
    

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

