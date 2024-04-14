from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')

def nosotros_view(request):
    return render(request, 'home/nosotros.html')

def contacto_view(request):
    return render(request, 'home/contacto.html')

def appMovil_view(request):
    return render(request, 'apps/appMovil.html')

def appWeb_view(request):
    return render(request, 'apps/appWeb.html')

def deskopIoT_view(request):
    return render(request, 'apps/deskopIoT.html')
