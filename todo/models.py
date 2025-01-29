from django.db import models
from django.conf import settings 

class Todo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    content = models.CharField(max_length=100) 
    is_completed = models.BooleanField(default=False) 
    select_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} - {'Completed' if self.is_completed else 'Incomplete'}"

