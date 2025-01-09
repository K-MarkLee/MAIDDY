from django.db import models
from django.conf import settings

class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)    
    select_date = models.DateField(blank=False)  #반드시 날짜가 입력
    time = models.TimeField()
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title