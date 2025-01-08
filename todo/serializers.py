
from .models import Todo
from rest_framework import serializers



# 모델을 직렬화하여 API에서 반환할 수 있도록 설정
class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # 유저 정보를 read_only로 설정
    class Meta:
        model = Todo
        fields = ['id', 'user', 'content', 'select_date', 'is_completed', 'created_at']
        read_only_fields = ['user', 'created_at'] # 유저 정보는 수정 불가능

