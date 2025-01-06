from django.db import models
from django.conf import settings 

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #유저 모델
    title = models.CharField(max_length=100) #To-Do 제목
    completed = models.BooleanField(default=False) # 완료 여부 # 체크리스
    select_date = models.DateField() # 입력한 날짜
    created_at = models.DateTimeField(auto_now_add=True) # 생성일자
    updated_at = models.DateTimeField(auto_now=True) # 수정일자
    
    
    def __str__(self):
        return f"{self.title} - {"Completed" if self.completed else "pending"}" # 제목 - 완료 여부
    