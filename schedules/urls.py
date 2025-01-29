from django.urls import path
from . import views

app_name = "schedules"

urlpatterns = [
    path('', views.schedule_list, name='schedule-list'), 
    path('pinned/', views.schedule_pinned, name='schedule-pinned'),  
    path('create/', views.schedule_create, name='schedule-create'),  
    path('update/', views.schedule_update, name='schedule-update'),  
    path('detail/<int:schedule_id>/', views.schedule_detail, name='schedule-detail'), 
    path('delete/<int:schedule_id>/', views.schedule_delete, name='schedule-delete'), 
]
    


