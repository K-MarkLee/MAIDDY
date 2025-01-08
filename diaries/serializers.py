from .models import Diary
from rest_framework import serializers


class DiarySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # 유저 정보를 read_only로 설정
    class Meta:
        model = Diary
        fields = ['id', 'user', 'title', 'content', 'select_date']
        read_only_fields = ['id','user', 'created_at', 'updated_at', 'select_date'] # 유저 정보는 수정 불가능


