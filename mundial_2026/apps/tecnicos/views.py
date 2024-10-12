from django.shortcuts import render

def tecnicos_view(request):
    return render(request, 'tecnicos.html')