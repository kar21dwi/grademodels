from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework import routers
from BackEnd.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BackEnd.api.urls')),
]
