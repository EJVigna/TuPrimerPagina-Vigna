from django.urls import path
from PrimerWeb import views

app_name = 'PrimerWeb'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('Club/', views.Club, name='Club'),
    path('Jugadores/', views.Jugador, name='Jugadores'),
    path('Deporte/', views.Deporte, name='Deporte'),
    path('CargaDeporte/', views.Carga_Deporte, name='Cargadeporte'),
    path('CargaClub/', views.Carga_Club, name='Cargaclub'),
    path('CargaJugador/', views.Carga_Jugador, name='Cargajugador'),
    path('fechaagora/', views.fecha_actual, name='fecha_actual')
]
