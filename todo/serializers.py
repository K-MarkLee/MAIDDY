from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'user', 'content', 'select_date', 'is_completed']
        read_only_fields = ['id', 'user', 'created_at']

