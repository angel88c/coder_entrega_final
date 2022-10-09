from django import forms
from ckeditor.fields import RichTextField

class PageForm(forms.Form):
    titulo =    forms.CharField(max_length = 50)
    subtitulo = forms.CharField(max_length = 50)
    cuerpo =    RichTextField()
    autor =     forms.CharField(max_length = 50)
    fecha =     forms.DateField()
    imagen =    forms.ImageField()