from django import forms
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PageForm(forms.Form):
    titulo =    forms.CharField(max_length = 50)
    subtitulo = forms.CharField(max_length = 50)
    cuerpo =    RichTextField()
    autor =     forms.CharField(max_length = 50)
    fecha =     forms.DateField()
    imagen =    forms.ImageField()

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Ingresar Contraseña',  widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field:"" for field in fields}