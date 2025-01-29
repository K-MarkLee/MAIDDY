from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('list/', views.todo_list, name='todo-list'), 
    path('checkbox/', views.todo_checkbox, name='todo-checkbox'),  
    path('create/', views.todo_create, name = 'todo-create'), 
    path('delete/<int:todo_id>/', views.todo_delete, name='todo-delete'),  
]