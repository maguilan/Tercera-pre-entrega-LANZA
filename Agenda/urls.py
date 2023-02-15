from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('conciertos/', conciertos, name='conciertos'),
    path('museos/', museos, name='museos'),
    path('artistas/', artistas, name='artistas'),
    path('vida-nocturna/', vida_nocturna, name='vida-nocturna'),

]