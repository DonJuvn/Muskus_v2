from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

from . import views
from .views import Search

urlpatterns = [
    path('', views.home, name='home'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('uni/', views.uni, name='uni'),
    path('search/', views.Search.as_view(), name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)