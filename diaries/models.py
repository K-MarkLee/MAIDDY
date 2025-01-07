from django.db import models
from django.conf import settings

class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'diaries') #  User 모델과 1:N 관계(유저가 삭제되면 다이어리도 삭제)
    title = models.CharField(max_length=30, blank=True, null=True) # 제목(선택) ## null 값 해도 되는가?
    content = models.TextField() # 내용
    select_date = models.DateField() # 입력한 날짜
    created_at = models.DateTimeField(auto_now_add = True) # 생성일자
    # updated_at = models.DateTimeField(auto_now = True) # 수정일자 현재 수정기능 미 구현으로 인한 주석처리
    
    
    def __str__(self):
        return f"{self.select_date} - {self.title if self.title else 'Untitled'}" # 날짜 - 제목