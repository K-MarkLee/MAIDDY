from django.db import models
from django.conf import settings 

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #유저 모델
    content = models.CharField(max_length=100) #To-Do 할 일 작성
    select_date = models.DateField() # 입력한 날짜
    created_at = models.DateTimeField(auto_now_add=True) # 생성일자

    
    
    def __str__(self):
        return self.content
    
class CheckList(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='checklists')  # Todo와 연결
    content = models.TextField()  # 체크리스트 내용
    checked = models.BooleanField(default=False)  # 완료 여부


def __str__(self):
    return f"{self.content} - {'Checked' if self.checked else 'Unchecked'}"

    