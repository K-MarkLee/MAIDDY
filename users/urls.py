from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView



app_name = "users"

urlpatterns = [
    path('create/', views.user_create, name='user_create'),  # 회원가입
    path('login/', views.login, name='user_login'),  # 로그인

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 프론트에서 필요함. (로그인 토큰 갱신)

]
