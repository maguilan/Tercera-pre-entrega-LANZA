from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    
class Meta:

    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = {k: '' for k in fields}

class UserEditForm(forms.Form):

    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:

        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        # exclude = ['password1', 'password2']
        help_texts = {k: '' for k in fields}
