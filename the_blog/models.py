from django.db import models
from django.db.models import Model

# Create your models here.
class Page(Model):
    titulo = models.CharField(max_length = 50)
    subtitulo = models.CharField(max_length = 50)
    cuerpo = models.CharField(max_length = 200)
    autor = models.CharField(max_length = 50)
    fecha = models.DateField()
    imagen = models.ImageField()

class Usuario(Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=100)