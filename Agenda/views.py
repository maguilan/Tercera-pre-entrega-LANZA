from django.shortcuts import render, redirect
from .forms import ArtistaFormulario, ConciertoFormulario, MuseoFormulario, VidaNocturnaForm
from .models import Artista, Concierto, Museo, VidaNocturna
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'Agenda/inicio.html')

def conciertos(request):
    mis_conciertos = Concierto.objects.all()

    if request.method == 'POST':
        mi_formulario = ConciertoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            concierto = Concierto(genero = informacion['genero'], 
                              banda = informacion['banda'], 
                              lugar = informacion['lugar'], 
                              fecha_concierto = informacion['fecha_concierto'],
                              pasado = informacion['pasado'])
            concierto.save()

            nuevo_concierto = {'genero': informacion['genero'], 'banda': informacion[concierto], 'lugar': informacion['lugar'], 
                              'fecha_concierto': informacion['fecha_concierto'],
                              'pasado': informacion['pasado']}
            return render (request, 'Agenda/concierto-formulario.html', {'formulario_concierto': mi_formulario, 'nuevo_concierto': nuevo_concierto, 'mis_conciertos': mis_conciertos})
        
        else:
            mi_formulario = ConciertoFormulario()

        return render(request, 'Agenda/concierto-formulario.html', {'formulario_concierto': mi_formulario, 'mis_conciertos': mis_conciertos})




def museos(request):
    return render(request, 'Agenda/museo-formulario.html')
    
def artistas(request):
    return render(request, 'Agenda/artista-formulario.html')

def vida_nocturna(request):
    return render(request, 'Agenda/vida-nocturna-formulario.html')

def artista_formulario(request):

    if request.method == 'POST':
        mi_formulario = ArtistaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            artista = Artista(nombre = informacion['nombre'], 
                              apellido = informacion['apellido'], 
                              email = informacion['email'], 
                              profesion = informacion['profesion'])
            artista.save()
            return redirect('inicio')

        
    mi_formulario = ArtistaFormulario()
    return render(request, 'Agenda/artista-formulario.html', {'formulario_artista': mi_formulario})

def concierto_formulario(request):

    if request.method == 'POST':
        mi_formulario = ConciertoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            concierto = Concierto(genero = informacion['genero'], 
                              banda = informacion['banda'], 
                              lugar = informacion['lugar'], 
                              fecha_concierto = informacion['fecha_concierto'],
                              pasado = informacion['pasado'])
            concierto.save()
            return redirect('inicio')

        
    mi_formulario = ConciertoFormulario()
    return render(request, 'Agenda/concierto-formulario.html', {'formulario_concierto': mi_formulario})

def museo_formulario(request):

    if request.method == 'POST':
        mi_formulario = MuseoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            museo = Museo(museo = informacion['museo'], 
                              obra = informacion['obra'], 
                              autor = informacion['autor'], 
                              fecha = informacion['fecha'])
            museo.save()
            return redirect('inicio')

        
    mi_formulario = MuseoFormulario()
    return render(request, 'Agenda/museo-formulario.html', {'formulario_museo': mi_formulario})

def vida_nocturna_formulario(request):

    if request.method == 'POST':
        mi_formulario = VidaNocturnaForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            evento= VidaNocturna(lugar = informacion['lugar'],
                                    evento = informacion['evento'], 
                                    fecha_de_evento = informacion['fecha_de_evento'])
            evento.save()
            return redirect('inicio')

        
    mi_formulario = VidaNocturnaForm()
    return render(request, 'Agenda/vida-nocturna-formulario.html', {'formulario_vidanocturna': mi_formulario})

def busqueda_genero(request):
    return render(request, 'Agenda/inicio.html')

def buscar(request):
    if request.GET['genero']:
        genero = request.GET['genero']
        resultado = Concierto.objects.filter(genero__icontains=genero)

        return render(request, 'Agenda/resultados-busqueda.html', {'conciertos': resultado, 'genero': genero})


    respuesta = 'No se encontró el género buscado'

    return HttpResponse(respuesta)
