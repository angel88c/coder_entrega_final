from datetime import date
from tkinter import image_names
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import PageForm, UserSignupForm, UserEditForm, AvatarForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    print('index')
    print(get_avatar(request))
    return render(request, 'the_blog/index.html', {'avatar': get_avatar(request)})

@login_required
def about(request):
    return render(request, 'the_blog/about.html', {'avatar': get_avatar(request)})

@login_required
def pages(request):
    pages = Page.objects.all()
    print(list(pages))
    return render(request, 'the_blog/pages.html', {'pages': pages, 'avatar': get_avatar(request)})

@login_required
def page(request, id):
    page = Page.objects.get(id=id)
    print('***')
    print(page)
    return render(request, 'the_blog/page.html', {'page': page, 'avatar': get_avatar(request)})

@login_required
def delete_page(request, id):
    page_to_delete = Page.objects.get(id=id)
    page_to_delete.delete()
    pages = Page.objects.all()
    return render(request, 'the_blog/pages.html', {'pages':pages, 'avatar': get_avatar(request)})

@login_required
def edit_page(request, id):
    current_page = Page.objects.get(id=id)
    print('*****')
    print(current_page)
    print(request.method)
    if request.method == 'POST':
        print('dentro del if')
        form_page = PageForm(request.POST)
        print(f'*****{form_page.is_valid()}*****')
        if form_page.is_valid():
            info = form_page.cleaned_data
            current_page.titulo = info['titulo']
            print(info['titulo'])
            current_page.subtitulo = info['subtitulo']
            print(info['subtitulo'])
            current_page.cuerpo = info['cuerpo']
            print(info['cuerpo'])
            current_page.autor = info['autor']
            print(info['autor'])
            current_page.fecha  = info['fecha']
            print(info['fecha'])
            current_page.imagen = info['imagen']
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
            'imagen': current_page.imagen.url
        })

        return render(request, 'the_blog/edit_page.html', {'formulario': form_page, 'page': current_page, 'avatar': get_avatar(request)})

@login_required
def new_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        print(form)
        print(f'**{form.is_valid()}**')
        if form.is_valid():
            page_info = form.cleaned_data
            print(page_info)
            titulo    = page_info['titulo']
            subtitulo = page_info['subtitulo']
            cuerpo    = page_info['cuerpo']
            autor     = page_info['autor']
            fecha     = page_info['fecha']
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
            return render(request, 'the_blog/new_page.html', {'formulario':form, 'mensaje': 'Formulario Invalido.'})
    else:
        page_form = PageForm()
        return render(request, 'the_blog/new_page.html', {'page_form':page_form, 'avatar': get_avatar(request)})

def login_request(request):

    if request.method == 'POST':
        #get the info from POST data
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user   = request.POST['username']
            passwd = request.POST['password']

            user1 = authenticate(username=user, password=passwd)
            if user1 is not None:
                login(request, user1)
                return render(request, 'the_blog/index.html', {'mensaje': f'Bienvenido {user1}'})
            else:
                return render (request, 'the_blog/login.html', {'formulario': form, 'mensaje':'Usuario o contraseña incorrectos.'})
        else:
            return render (request, 'the_blog/login.html', {'formulario': form, 'mensaje':'Usuario o contraseña incorrectos.'})
    else:
        form = AuthenticationForm()
        return render (request, 'the_blog/login.html', {'formulario': form})

def register_request(request):

    if request.method == 'POST':
        #get the info from POST data
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username   = form.cleaned_data['username']

            form.save()

            return render(request, 'the_blog/index.html', {'mensaje': f'Usuario {username} Creado.'})

        else:
            return render (request, 'the_blog/register.html', {'formulario': form, 'mensaje':'Formulario invalido.'})
    else:
        form = UserSignupForm()
        return render (request, 'the_blog/register.html', {'formulario': form, })

@login_required
def edit_user(request):

    #Obtengo el usuario que está logueado
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        print("The form is valid? " +str(form.is_valid()))
        if form.is_valid():
            info = form.cleaned_data
            print(info)
            usuario.email = info['email']
            usuario.password1=info['password1']
            usuario.password2=info['password2']
            usuario.name=info['name']
            usuario.last_name=info['last_name']
            usuario.save()

            return render(request, 'the_blog/index.html', {'mensaje':'Usuario modificado correctamente.'})
        else:
            return render(request, 'the_blog/edit_user.html', {'mensaje':'Formulario invalido.'})
    else:
        form = UserEditForm(instance=usuario)

        return render(request, 'the_blog/edit_user.html', {'formulario':form, 'usuario':usuario, 'avatar': get_avatar(request)})

@login_required
def create_avatar(request):
    usuario = request.user

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():

            old_avatar = Avatar.objects.filter(user=request.user)

            if len(old_avatar) > 0:
                old_avatar[0].delete()

            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'the_blog/index.html', {'usuario': usuario, 'mensaje':'Avatar Agregado exitosamente', 'imagen':avatar.imagen.url})
        else:
            return render(request, 'the_blog/create_avatar.html', {'formulario':form, 'mensaje': 'Formulario Invalido.'})
    else:
        form = AvatarForm()
        return render(request, 'the_blog/create_avatar.html', {'formulario':form, 'usuario':usuario, 'avatar': get_avatar(request)})

def get_avatar(request):
    avatar_list = Avatar.objects.filter(user=request.user)
    print(avatar_list)
    if len(avatar_list) > 0:
        avatar_image = avatar_list[0].imagen.url
    else:
        avatar_image = '/media/avatares/default_avatar/default.png'

    print(avatar_image)
    return avatar_image