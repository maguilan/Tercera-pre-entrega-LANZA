from django.db import models

# Create your models here.

class Concierto(models.Model):
    
    genero = models.CharField(max_length=40)
    banda = models.CharField(max_length=40)
    lugar = models.CharField(max_length=40)
    fecha_concierto = models.DateField()
    pasado = models.BooleanField()

    def __str__(self):
        return self.banda + '(' + str(self.lugar) + ')'

class Museo(models.Model):

    museo = models.CharField(max_length=30)
    obra = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    fecha = models.DateField()

    def __str__(self):
        return self.museo 

class Artista(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + ' ' + str(self.apellido) 


class VidaNocturna(models.Model):
    
    lugar = models.CharField(max_length=30)
    evento = models.CharField(max_length=30)
    fecha_de_evento = models.DateField()

    class Meta:
        verbose_name_plural = 'Vidas Nocturnas'
    
class Avatar(models.Model):