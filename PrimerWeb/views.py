from django.shortcuts import render
from PrimerWeb import models



# def padre (request):
#     return render(request, 'padre.html')

def inicio (request):
    return render(request, 'PrimerWeb/inicio.html')

def Club (request):
    return render(request, 'PrimerWeb/Club.html')

def Jugadores (request):
    return render(request, 'PrimerWeb/Jugadores.html')

def Deporte (request):
    return render(request, 'PrimerWeb/Deporte.html')