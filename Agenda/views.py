from django.shortcuts import render, redirect
from .forms import ArtistaFormulario, ConciertoFormulario, MuseoFormulario, VidaNocturnaForm, MyUserCreationForm, UserEditForm
from .models import Artista, Concierto, Museo, VidaNocturna
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

            nuevo_concierto = {'genero': informacion['genero'], 'banda': informacion['banda'], 'lugar': informacion['lugar'], 
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

# def concierto_formulario(request):

#     if request.method == 'POST':
#         mi_formulario = ConciertoFormulario(request.POST)

#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             concierto = Concierto(genero = informacion['genero'], 
#                               banda = informacion['banda'], 
#                               lugar = informacion['lugar'], 
#                               fecha_concierto = informacion['fecha_concierto'],
#                               pasado = informacion['pasado'])
#             concierto.save()
#             return redirect('inicio')

        
#     mi_formulario = ConciertoFormulario()
#     return render(request, 'Agenda/concierto-formulario.html', {'formulario_concierto': mi_formulario})

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

def leer_artistas(request):
    artistas = Artista.objects.all()

    contexto= {"artistas": artistas}
    return render(request, 'Agenda/leer-artistas.html', contexto)

def eliminar_artista(request, artista_id):
    artista= Artista.objects.get(id=artista_id)
    artista.delete()

    artistas = Artista.objects.all()

    contexto = {'artistas': artistas}

    return render(request, 'Agenda/leer-artistas.html', contexto)

def editar_artista(request, artista_id):
    artista= Artista.objects.get(id=artista_id)
    
    if request.method == 'POST':
        mi_formulario = ArtistaFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            artista.nombre = informacion['nombre']
            artista.apellido = informacion['apellido']
            artista.email = informacion['email']
            artista.profesion = informacion['profesion']
        
            artista.save()
            
            artistas = Artista.objects.all()
            contexto = {'artistas': artistas }

        return render(request, 'Agenda/leer-artistas.html', contexto)
    
    else:
        mi_formulario = ArtistaFormulario(initial= {'nombre': artista.nombre, 'apellido': artista.apellido, 'email': artista.email, 'profesion': artista.profesion})

        artistas = Artista.objects.all()
        contexto = {'mi_formulario': mi_formulario, 'artista.id': artista.id, 'artistas': artistas }
    
    return render(request, 'Agenda/leer-artistas.html', contexto)

class ConciertoList(LoginRequiredMixin, ListView):

    model = Concierto
    template_name = 'Agenda/conciertos-list.html'

class ConciertoDetalle(DetailView):

    model = Concierto
    template_name = 'Agenda/concierto-detalle.html'

class ConciertoCreacion(CreateView):

    model = Concierto
    template_name = 'Agenda/concierto-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['genero', 'banda', 'lugar', 'fecha_concierto', 'pasado']

class ConciertoUpdate(UpdateView ):

    model = Concierto
    template_name = 'Agenda/concierto-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['genero', 'banda', 'lugar', 'fecha_concierto', 'pasado']

class ConciertoDelete(DeleteView):

    model = Concierto
    template_name = 'Agenda/concierto-eliminar.html'
    success_url = reverse_lazy('inicio')

def login_request(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                contexto = {'mensaje': f'Bienvenido {usuario}'}
                return render(request, 'Agenda/inicio.html', contexto)
            else:
                contexto = {'mensaje': f'Error, datos inconrrectos', 'form': form}
                return render(request, 'Agenda/login.html', contexto)
        
        else:
            contexto = {'mensaje': f'Los datos son erróneos', 'form': form}
            return render(request, 'Agenda/login.html', contexto)
    
    contexto = {'form': form}
    return render(request, 'Agenda/login.html', contexto)

def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            contexto = {'mensaje': f'Usuario Creado Correctamente'}
            return render(request, 'Agenda/inicio.html', contexto)
        
    else:
        form = MyUserCreationForm()
        contexto = {'form': form }
        return render(request, 'Agenda/registro.html', contexto)
            

@login_required
def editar_perfil(request):
    usuario = User.objects.get(username=request.user)

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']

            usuario.save()

            return redirect('/')

    else:

        mi_formulario = UserEditForm(initial={'username': usuario.username, 
                                            'email':usuario.email, 
                                            'first_name': usuario.first_name,
                                            'last_name': usuario.last_name})

    return render(request, 'Agenda/editar-perfil.html', {'mi_formulario': mi_formulario, 'usuario': usuario})



