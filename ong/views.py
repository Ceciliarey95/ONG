from django.shortcuts import render
from django.contrib import admin



def Index(request):
    return render(request, 'index.html')

def fotos(request):
    return render(request, 'fotos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

