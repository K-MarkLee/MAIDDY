from django.db import models
from django.conf import settings

class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'diaries') 
    title = models.CharField(max_length=30, blank=True, null=True) 
    content = models.TextField() 
    select_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add = True) 
    updated_at = models.DateTimeField(auto_now = True) 
    
    def __str__(self):
        return f"{self.select_date} - {self.title if self.title else 'Untitled'}"
    
