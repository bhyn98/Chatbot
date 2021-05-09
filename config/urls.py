from django.conf.urls import url, include
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from ChatbotApp import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.user_list),
    # path('Users/<int:pk>', views.user),
    # path('', ChatbotApp.views.login, name='login'),
    # path('chatPage/', ChatbotApp.views.chatPage, name='chatPage'),
    # path('register/', ChatbotApp.views.register, name='register'),
    # path('grades/', ChatbotApp.views.grades, name='grades'),
]
