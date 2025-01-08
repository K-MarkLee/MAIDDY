
from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('<int:diary_id>/', views.diary_detail, name='diary-detail'),  # 다이어리  조회
    path('create/', views.diary_create, name='diary-create'),  # 다이어리 생성
    path('update/', views.diary_update, name='diary-update'),  # 다이어리 수정
    path('ai/chatbot/comment/', views.comment_link, name='comment'),  # 코멘트로 이동
]


