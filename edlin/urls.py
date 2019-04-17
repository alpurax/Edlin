from django.contrib import admin
from django.urls import path, include
from body.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('body/', include('body.urls')),
    path('', index),
]
