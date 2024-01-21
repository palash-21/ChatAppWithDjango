from django.urls import path
from .views import register, loginView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginView, name='login'),
]
