from django.shortcuts import render

def posiciones_view(request):
    return render(request, 'posiciones.html')