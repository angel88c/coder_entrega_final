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
    print()

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
