from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Page(Model):
    titulo = models.CharField(max_length = 50)
    subtitulo = models.CharField(max_length = 50)
    cuerpo =  RichTextField()
    autor = models.CharField(max_length = 50)
    fecha = models.DateField()
    imagen = models.ImageField()

class Usuario(Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    text_message = models.CharField(max_length=100, default='')

class Avatar(Model):
    #Pointing to user, erase all whe user deleted
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares')