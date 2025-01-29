from .models import Diary
from rest_framework import serializers

class DiarySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Diary
        fields = ['id', 'user', 'title', 'content', 'select_date']
        read_only_fields = ['id','user', 'created_at', 'updated_at']


