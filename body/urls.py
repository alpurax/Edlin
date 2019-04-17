from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import index

app_name = 'body'

urlpatterns = [
    path('',index),
]