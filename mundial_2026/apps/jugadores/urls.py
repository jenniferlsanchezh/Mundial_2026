from django.urls import path
from . import views

urlpatterns = [
    path('jugadores/', views.jugadores_view, name='jugadores'),
]