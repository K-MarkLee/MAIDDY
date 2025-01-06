from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # 유저 정보를 read_only로 설정
    class Meta:
        model = Diary
        fields = ['id', 'title', 'content', 'select_date']
