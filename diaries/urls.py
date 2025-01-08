
from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.diary_detail, name='diary-detail'),  # 다이어리  조회 (GET) (api/diaries/detail/?date=2025-01-01)
    path('update/', views.diary_update, name='diary-update'),  # 다이어리 생성

]


