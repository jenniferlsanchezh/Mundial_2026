from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.equipos_view, name='equipos'),
]
