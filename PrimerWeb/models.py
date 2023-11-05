from django.db import models

# Create your models here.

class Deporte (models.Model):
    
    Nombre = models.CharField(max_length=40)
    Jugadores = models.IntegerField()
    
class Jugador (models.Model):
    
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Edad = models.IntegerField()
    Diciplina = models.CharField(max_length=40)
    
class Club (models.Model):
    
    Nombre = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=40)
    Fundacion = models.IntegerField()
    Socios = models.IntegerField()
