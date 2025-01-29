from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "users"

urlpatterns = [
    path('create/', views.user_create, name='user_create'),  
    path('login/', views.login, name='user_login'),  
    path('logout/', views.logout, name='user_logout'),  
    path('delete/', views.delete_account, name='user_delete'),  

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

]
