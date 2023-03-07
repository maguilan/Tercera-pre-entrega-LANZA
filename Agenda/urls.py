from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    # path('', inicio, name='inicio'),
    # path('conciertos/', conciertos, name='conciertos'),
    # path('museos/', museo_formulario, name='museos'),
    #path('artistas/', artista_formulario, name='artistas'),
    # path('vida-nocturna/', vida_nocturna_formulario, name='vida-nocturna'),
    path('artista-formulario', artista_formulario, name='artista-formulario'),
    # path('concierto-formulario', concierto_formulario, name='concierto-formulario'),
    path('', ConciertoList.as_view(), name='inicio'),
    path('detalle/<pk>', ConciertoDetalle.as_view(), name='detalle'),
    path('nuevo/', ConciertoCreacion.as_view(), name='nuevo'),
    path('editar/<pk>', ConciertoUpdate.as_view(), name='editar'),
    path('eliminar/<pk>', ConciertoDelete.as_view(), name='eliminar'),
    path('login', login_request, name="login"),
    path('registro', register, name="registro"),
    path('logout', LogoutView.as_view(template_name='Agenda/logout.html'), name="logout"),
    path('editar-perfil', editar_perfil, name='editar-perfil'),
    path('agregar-avatar', agregar_avatar, name='agregar-avatar')
]