from rest_framework import serializers
from .models import Diary, Comment

class DiarySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # 유저 정보를 read_only로 설정
    class Meta:
        model = Diary
        fields = ['id', 'title', 'content', 'select_date']
        read_only_fields = ['user', 'created_at', 'updated_at'] # 유저 정보는 수정 불가능

class CommentSerializer(serializers.ModelSerializer):
    #챗봇 url 링크만 직렬화
    chatbot_url = serializers.URLField()
    
    class Meta:
        model = Comment
        fields = ['id', 'chatbot_url']