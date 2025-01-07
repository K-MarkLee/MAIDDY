from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # 유저 정보를 read_only로 설정
    class Meta:
        model = Diary
        fields = ['id','user', 'title', 'content', 'select_date', 'created_at','updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at'] # 유저 정보는 수정 불가능
