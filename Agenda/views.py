from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'Agenda/inicio.html')

def conciertos(request):
    return render(request, 'Agenda/conciertos.html')

def museos(request):
    return render(request, 'Agenda/museos.html')
    
def artistas(request):
    return render(request, 'AppCoder/artistas.html')

def vida_nocturna(request):
    return render(request, 'AppCoder/vida-nocturna.html')