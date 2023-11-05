from django.shortcuts import render
from PrimerWeb import models
from forms import *


def inicio (request):
    return render(request, 'PrimerWeb/inicio.html')

def Club (request):
    return render(request, 'PrimerWeb/Club.html')

def Jugadores (request):
    return render(request, 'PrimerWeb/Jugadores.html')

def Deporte (request):
    return render(request, 'PrimerWeb/Deporte.html')

def Carga_Deporte (request):
    if request.method == 'POST':
        deporte = CargaDeporte(request.post)
        print(deporte)
        if deporte.is_valid:
            informacion = deporte.cleaned_data
            deporte = Deporte(informacion["deporte"], informacion["jugadores"])
            deporte.save()
            return render(request, 'PrimerWeb/inicio.html')
    else:
        deporte = CargaDeporte()
        return render(request, 'PrimerWeb/Carga_Deporte.html',{'deporte':deporte}) 
    
def Carga_Jugador (request):
    if request.method == 'POST':
        jugador = Cargajugador(request.post)
        print(jugador)
        if jugador.is_valid:
            informacion = jugador.cleaned_data
            jugador = Jugadores(informacion["nombre"], informacion["apellido"], informacion["edad"], informacion["diciplina"])
            jugador.save()
            return render(request, 'PrimerWeb/inicio.html')
    else:
        jugador = Cargajugador()
        return render(request, 'PrimerWeb/Carga_Jugador.html',{'jugador':jugador})
    
def Carga_Club (request):
    if request.method == 'POST':
        club = CargaClub(request.post)
        print(club)
        if club.is_valid:
            informacion = club.cleaned_data
            club = Club(informacion["nombre"], informacion["ciudad"], informacion["fundacion"], informacion["socios"])
            club.save()
            return render(request, 'PrimerWeb/inicio.html')
    else:
        club = CargaClub()
        return render(request, 'PrimerWeb/Carga_Club.html',{'club':club})
            