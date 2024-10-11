from django.shortcuts import render

# Create your views here.
def tecnicos_home(request):
    return render(request,'tecnicos/tecnicos_home.html')
