from django.db import models
from django.conf import settings 

class Todo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #유저 모델 연결
    content = models.CharField(max_length=100) #To-Do 할 일
    is_completed = models.BooleanField(default=False) # 완료 여부
    select_date = models.DateField() # 할일 의 날짜
    created_at = models.DateTimeField(auto_now_add=True) # 생성일자

    def __str__(self):
        return f"{self.content} - {'Completed' if self.is_completed else 'Incomplete'}" # 할일 - 완료 여부

