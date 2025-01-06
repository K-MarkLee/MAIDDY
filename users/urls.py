from django.urls import path, include
from . import views
from rest_framework import urls

app_name = "users"

urlpatterns = [
    path('create/', views.user_create, name='user_create'),  # 회원가입
    path('login/', views.login, name='user_login'),  # 로그인
    path('logout/', views.logout, name='user_logout'),  # 로그아웃
    path('profile/<str:username>/', views.profile, name='user_profile'),  # 프로필 조회
    # path('profile/update/', views.profile_update, name='user_profile_update'),  # 프로필 수정

    # 비밀번호 재설정 API 추가
    path('password-reset-request/', views.password_reset_request, name='password_reset_request'),
    path('password-reset/', views.password_reset_confirm, name='password_reset_confirm'),

]
