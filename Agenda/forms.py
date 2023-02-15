from django import forms

class ArtistaFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class ConciertoFormulario(forms.Form):

    genero = forms.CharField(max_length=40)
    banda = forms.CharField(max_length=40)
    lugar = forms.CharField(max_length=40)
    fecha_concierto = forms.DateField()
    pasado = forms.BooleanField()

class MuseoFormulario(forms.Form):

    museo = forms.CharField(max_length=30)
    obra = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    fecha = forms.DateField()

class VidaNocturnaForm(forms.Form):
    
    lugar = forms.CharField(max_length=30)
    evento = forms.CharField(max_length=30)
    fecha_de_evento = forms.DateField()


