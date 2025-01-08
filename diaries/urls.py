
from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('detail/', views.diary_detail, name='diary-detail'),  # 다이어리  조회 (GET) (api/diaries/detail/?date=2025-01-01)
    path('create/', views.diary_create_and_update, name='diary-create'),  # 다이어리 생성
    path('update/', views.diary_update, name='diary-update'),  # 다이어리 수정 
]


