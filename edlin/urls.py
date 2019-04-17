from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from body.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('body/', include('body.urls', namespace="body"), name='body'),
    path('', index),
    path('accounts/profile/', index),
    #path('body/login/', LoginView.as_view(), name='login'),
    #path('body/logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
