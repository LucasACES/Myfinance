from django.shortcuts import render

# Create your views here.

def homeLogged(request):
    return render(request, 'html/home.html')