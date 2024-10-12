from django.urls import path  
from . import views

urlpatterns = [
    path('', views.posiciones_home, name='posiciones_home'),
]
