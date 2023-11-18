from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(models.Club)
# admin.site.register(models.Deporte)
# admin.site.register(models.Jugador)

@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Jugadores')
    list_filter = ('Nombre', 'Jugadores')
    search_fields = ('Nombre', 'Jugadores')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'Edad', 'Diciplina')
    list_filter = ('Nombre', 'Apellido', 'Diciplina')
    search_fields = ('Nombre', 'Apellido')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Ciudad', 'Fundacion', 'Socios')
    list_filter = ('Nombre', 'Ciudad', 'Fundacion')
    search_fields = ('Nombre', 'Fundacion')
    
