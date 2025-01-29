from django.contrib import admin
from django.urls import path, include
from .views import ChatbotAPIView, FeedbackAPIView, RecommendAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
]
=======
    path("api/users/", include('users.urls')),
    path("api/diaries/", include('diaries.urls')),
    path("api/todo/", include('todo.urls')),
    path("api/schedules/", include('schedules.urls')),
  
  
    path('ai/chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
    path('ai/feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('ai/recommend/', RecommendAPIView.as_view(), name='recommend'),
]
>>>>>>> mvp
