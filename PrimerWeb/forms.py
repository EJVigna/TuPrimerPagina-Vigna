from django import forms
from .models import *

class CargaDeporte(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ['Nombre', 'Jugadores']
    
    
class Cargajugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['Nombre', 'Apellido', 'Edad', 'Diciplina']
    
class CargaClub(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['Nombre','Ciudad','Fundacion','Socios']
    