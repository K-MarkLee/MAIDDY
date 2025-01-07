from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('todo/<str:date>/', views.todo_list, name='todo-list'),  # 할 일 목록 표시 (GET)
    path('create/', views.todo_create, name = 'todo-create'), # 할 일 생성 (POST)
    path('<int:todo_id>/update/', views.todo_update, name='todo-update'),  # 할 일 수정 (PUT)
    path('<int:todo_id>/delete/', views.todo_update, name='todo-delete'),  # 할 일 삭제 (DELETE)
]