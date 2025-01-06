from . import views
from django.urls import path

app_name = 'diaries'
urlpatterns =  [
    path('', views.diary_list, name = 'diary-list'),
    path('create/', views.diary_create, name = 'diary-create'),
    path('<int:diary_id>/', views.diary_detail, name = 'diary-detail'),
]