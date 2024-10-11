from django.shortcuts import render

# Create your views here.
def equipos_home(request):
    return render(request,'equipos/equipos_home.html')
