from django.shortcuts import render, redirect
from .models import Club, Jugador, Deporte
from .forms import CargaDeporte, Cargajugador, CargaClub



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
        return render(request, 'Carga_Jugador.html', {'form':form})
            