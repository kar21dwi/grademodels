from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from BackEnd.api import views
from django.urls import reverse



urlpatterns = [

   path('updategraderun/', views.updateGradeRun),

]