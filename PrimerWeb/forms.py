from django import forms
from .models import *

class CargaDeporte(forms.Form):
    Nombre = forms.CharField()
    Jugadores = forms.IntegerField()
    
class Cargajugador(forms.Form):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    Edad = forms.IntegerField()
    Diciplina = forms.CharField()
    
class CargaClub(forms.Form):
    Nombre = forms.CharField()
    Ciudad = forms.CharField()
    Fundacion = forms.IntegerField()
    Socios = forms.IntegerField()