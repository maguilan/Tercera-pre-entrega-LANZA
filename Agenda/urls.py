from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('conciertos/', conciertos, name='conciertos'),
    path('museos/', museo_formulario, name='museos'),
    path('artistas/', artista_formulario, name='artistas'),
    path('vida-nocturna/', vida_nocturna_formulario, name='vida-nocturna'),
    path('artista-formulario', artista_formulario, name='artista-formulario'),
    #path('concierto-formulario', concierto_formulario, name='concierto-formulario'),
    path('museo-formulario', museo_formulario, name='museo-formulario'),
    path('vida-nocturna-formulario', vida_nocturna_formulario, name='vida-nocturna-formulario'),
    path('busqueda-genero/', busqueda_genero, name= 'busqueda-genero'),
    path('buscar', buscar, name='buscar')
]