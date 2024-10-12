from django.shortcuts import render

def equipos_view(request):
    return render(request, 'equipos.html')