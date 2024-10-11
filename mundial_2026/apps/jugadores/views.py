from django.shortcuts import render

# Create your views here.
def jugadores_home(request):
    return render(request,'jugadores/jugadores_home.html')
