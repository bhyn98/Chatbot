from django.urls import path, include
import ChatbotApp
from ChatbotApp import views
from django.contrib import admin


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.user_list),
    path('users/<int:pk>', views.user),
    path('', ChatbotApp.views.login, name='login'),
    path('login/', ChatbotApp.views.login),
    path('chatPage/', ChatbotApp.views.chatPage, name='chatPage'),
    path('register/', ChatbotApp.views.register, name='register'),
    path('grades/', ChatbotApp.views.grades, name='grades'),
    path('admin/', admin.site.urls),

]
