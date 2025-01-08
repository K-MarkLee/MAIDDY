from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('list/', views.todo_list, name='todo-list'),  # 할 일 목록 조회 (GET)  (api/todo/list/?date=2025-01-01)
    path('checkbox/', views.todo_checkbox, name='todo-checkbox'),  # 할 일 완료 여부 변경 (PATCH) (api/todo/checkbox/?date=2025-01-01&todo_id=1)
    path('create/', views.todo_create, name = 'todo-create'), # 할 일 생성 (POST)
    path('delete/<int:todo_id>/', views.todo_delete, name='todo-delete'),  # 할 일 삭제 (DELETE)
]