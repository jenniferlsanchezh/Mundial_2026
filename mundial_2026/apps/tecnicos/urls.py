from django.urls import path  
from . import views

urlpatterns = [
    path('', views.tecnicos_home, name='tecnicos_home'),
]