from django.urls import path  
from . import views

urlpatterns = [
    path('', views.equipos_home, name='equipos_home'),
]