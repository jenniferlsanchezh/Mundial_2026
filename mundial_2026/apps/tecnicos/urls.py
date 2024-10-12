from django.urls import path
from . import views

urlpatterns = [
    path('tecnicos/', views.tecnicos_view, name='tecnicos'),
]