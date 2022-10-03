from django import forms

class PageForm(forms.Form):
    titulo =    forms.CharField(max_length = 50)
    subtitulo = forms.CharField(max_length = 50)
    cuerpo =    forms.CharField(max_length = 200)
    autor =     forms.CharField(max_length = 50)
    fecha =     forms.DateField()
    imagen =    forms.ImageField()