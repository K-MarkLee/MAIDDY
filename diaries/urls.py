from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.diary_detail, name='diary-detail'),  # 다이어리  조회
    path('diaries/create/', views.diary_create, name='diary-create'),  # 다이어리 생성
    path('diaries/update/', views.diary_update, name='diary-update'),  # 다이어리 수정정
    path('chatbot/ai/comment?year=n&month=n&day=n/', views.d, name='comment'),  # 코멘트로 이동동
]


