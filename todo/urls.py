from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('todo/<str:date>/', views.todo_list, name='todo'),  # 할 일 목록 표시 (GET)
    path('create/', views.todo_create, name = 'todo-create'), # 할 일 생성 (POST)
    path('delete/<int:todo_id>', views.todo_delete, name='todo-delete'),  # 할 일 삭제 (DELETE)
]