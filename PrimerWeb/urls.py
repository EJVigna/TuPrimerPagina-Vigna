from django.urls import path
from PrimerWeb import views


app_name = 'PrimerWeb'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('CargaDeporte/', views.Carga_Deporte, name='Carga deporte'),
    path('CargaClub/', views.Carga_Club, name='Carga club'),
    path('CargaJugador/', views.Carga_Jugador, name='Carga jugador'),
    path('Buscardeporte/', views.buscar_deporte, name='Buscar Deporte'),
    path('Buscarclub/', views.buscar_club, name='Buscar Club'),
]
