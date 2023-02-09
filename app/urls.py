from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('uni/', views.uni, name='uni'),
]