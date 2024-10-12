from django.shortcuts import render

def jugadores_view(request):
    return render(request, 'jugadores.html')