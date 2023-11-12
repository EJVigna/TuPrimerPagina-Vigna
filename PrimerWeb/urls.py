from django.urls import path
from PrimerWeb import views

app_name = 'PrimerWeb'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('CargaDeporte/', views.Carga_Deporte, name='Cargadeporte'),
    path('CargaClub/', views.Carga_Club, name='Cargaclub'),
    path('CargaJugador/', views.Carga_Jugador, name='Cargajugador'),
]
