from django.urls import path  
from . import views

urlpatterns = [
    path('', views.jugadores_home, name='jugadores_home'),
]
