from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView



app_name = "users"

urlpatterns = [
    path('create/', views.user_create, name='user_create'),  # 회원가입
    path('login/', views.login, name='user_login'),  # 로그인
    path('logout/', views.logout, name='user_logout'),  # 로그아웃

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 프론트에서 필요함. (로그인 토큰 갱신)

    # path('profile/<str:username>/', views.profile, name='user_profile'),  # 프로필 조회

]
