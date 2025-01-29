from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.diary_detail, name='diary-detail'), 
    path('update/', views.diary_update, name='diary-update'), 
]


