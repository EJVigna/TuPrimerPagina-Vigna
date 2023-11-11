from django.urls import path
from PrimerWeb import views

app_name = 'PrimerWeb'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('Club/', views.Club, name='Club'),
    path('Jugadores/', views.Jugadores, name='Jugadores'),
    path('Deporte/', views.Deporte, name='Deporte'),
    path('CargaDeporte/', views.Carga_Deporte, name='Carga deporte'),
    path('CargaClub/', views.Carga_Club, name='Carga club'),
    path('CargaJugador/', views.Carga_Jugador, name='Carga jugador'),
    path('fechaagora/', views.fecha_actual, name='fecha_actual')
]
