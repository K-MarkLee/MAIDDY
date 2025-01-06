from django.db import models
# from django.conf import settings 이것도 사용할 수 있으나, 아래 get 유저 모델로 하는 것이 보다 안정적
from django.contrib.auth.models import User 

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'diaries') #  User 모델과 1:N 관계(유저가 삭제되면 다이어리도 삭제)
    title = models.CharField(max_length=30, blank=None, Null = True) # 제목(선택)
    content = models.TextField() # 내용
    select_date = models.DateField() # 입력한 날짜
    created_at = models.DateTimeField(auto_now_add = True) # 생성일자
    # updated_at = models.DateTimeField(auto_now = True) # 수정일자 현재 수정기능 미 구현으로 인한 주석처리
    
    
    def __str__(self):
        return f"{self.select_date} - {self.title}" # 날짜 - 제목