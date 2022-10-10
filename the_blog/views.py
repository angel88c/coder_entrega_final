import datetime
from tkinter import image_names
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import PageForm
# Create your views here.
def inicio(request):
    return render(request, 'the_blog/index.html')

def about(request):
    return render(request, 'the_blog/about.html')

def pages(request):
    pages = Page.objects.all()
    print(list(pages))
    return render(request, 'the_blog/pages.html', {'pages': pages})

def page(request, id):
    page = Page.objects.get(id=id)
    print('***')
    print(page)
    return render(request, 'the_blog/page.html', {'page': page})

def delete_page(request, id):
    page_to_delete = Page.objects.get(id=id)
    page_to_delete.delete()
    pages = Page.objects.all()
    return render(request, 'the_blog/pages.html', {'pages':pages})

def edit_page(request, id):
    current_page = Page.objects.get(id=id)
    print('***')
    print(current_page)
    if request.method == 'POST':
        form_page = PageForm(request.POST)
        if form_page.is_valid:
            print(form_page.is_valid())
            info = form_page.cleaned_data
            current_page.titulo = info['titulo']
            print(info['titulo'])
            current_page.subtitulo = info['subtitulo']
            print(info['subtitulo'])
            #current_page.cuerpo = info['cuerpo']
            #print(info['cuerpo'])
            current_page.autor = info['autor']
            print(info['autor'])
            current_page.fecha  = info['fecha']
            print(info['fecha'])
            #current_page.imagen = info['imagen']
            #print(info['imagen'])

            current_page.save()
            pages = Page.objects.all()

            return render(request, 'the_blog/pages.html', {'pages': pages})
    else:
        form_page = PageForm(initial={
            'titulo': current_page.titulo,
            'subtitulo': current_page.subtitulo,
            'cuerpo': current_page.cuerpo,
            'autor': current_page.autor,
            'fecha': current_page.fecha,
            'imagen': current_page.imagen
        })

        return render(request, 'the_blog/edit_page.html', {'formulario': form_page, 'page': current_page})

def new_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid:
            page_info = form.cleaned_data
            print(page_info)
            titulo    = page_info['titulo']
            subtitulo = page_info['subtitulo']
            cuerpo    = page_info['cuerpo']
            autor     = page_info['autor']
            fecha     = datetime.now()
            imagen    = page_info['imagen']

            page = Page(titulo=titulo,
                        subtitulo=subtitulo,
                        cuerpo=cuerpo,
                        autor=autor,
                        fecha=fecha,
                        imagen=imagen)
            page.save()
            pages = Page.objects.all()
            return render(request, 'the_blog/pages.html', {'pages':pages})
    else:
        page_form = PageForm()
        return render(request, 'the_blog/new_page.html', {'page_form':page_form})
