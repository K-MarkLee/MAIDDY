from rest_framework import serializers
from .models import Todo, CheckList



class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = ['id', 'content', 'checked'] # 체크리스트 정보만 가져오기기


# 모델을 직렬화하여 API에서 반환할 수 있도록 설정
class TodoSerializer(serializers.ModelSerializer):
    checklists = CheckListSerializer(many=True, read_only=True) # 연결된 체크리스트 표시
    # user = serializers.StringRelatedField(read_only=True) # 유저 정보를 read_only로 설정
    class Meta:
        model = Todo
        fields = ['id', 'content',  'checklists']
        read_only_fields = ['user']
        