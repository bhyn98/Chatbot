from django.contrib import admin
from django.urls import path, include

import ChatbotApp
from . import views

urlpatterns = [
    path('login/', ChatbotApp.views.login, name='login'),
    path('chatPage/', ChatbotApp.views.chatPage, name='chatPage'),
    path('register/', ChatbotApp.views.register, name='register'),
    path('grades/', ChatbotApp.views.grades, name='grades'),
    path('admin/', views.site.urls),
]
