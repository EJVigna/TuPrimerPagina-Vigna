from django.shortcuts import render, redirect
from .models import Club, Jugador, Deporte
from .forms import CargaDeporte, Cargajugador, CargaClub
from django.http import HttpResponse

def inicio (request):
    return render (request, 'inicio.html')

def Carga_Deporte (request):
    if request.method == 'POST':
        form = CargaDeporte(request.POST)
        if form.is_valid():
            deporte = form.save()
            return redirect('PrimerWeb:inicio')
    else:
        form = CargaDeporte()
        return render(request, 'Carga_Deporte.html', {'form':form}) 
    
def Carga_Jugador (request):
    if request.method == 'POST':
        form = Cargajugador(request.POST)
        if form.is_valid():
            jugador = form.save()
            return redirect('PrimerWeb:inicio')
    else:
        form = Cargajugador()
        return render(request, 'Carga_Jugador.html', {'form':form}) 
    
def Carga_Club (request):
    if request.method == 'POST':
        form = CargaClub(request.POST)
        if form.is_valid():
            club = form.save()
            return redirect('PrimerWeb:inicio')
    else:
        form = CargaClub()
        return render(request, 'Carga_Club.html', {'form':form})
    
def buscar_deporte(request):

        if request.GET["Nombre"]:
            Nombre = request.GET['Nombre'] 
            deportes = Deporte.objects.filter(Nombre__icontains=Nombre)

            return render(request, "inicio.html", {"Nombre":Nombre, "Deporte":deportes})
        else:

	        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)
            