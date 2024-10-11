from django.shortcuts import render

# Create your views here.
def posiciones_home(request):
    return render(request,'posiciones/posiciones_home.html')
