# Readme.md

# Integrantes

### Arely Torres

### Angel Carreon

## Uso de la app

La aplicacion se llama **the_blog**, cuando se ejecuta 

```bash
python manage.py runserver
```
Se entra mediante [http://127.0.0.1:8000/the_blog/]()

### Rutas
```python
urlpatterns = [
    path('',                inicio,         name='inicio'),
    path('about/',          about,          name='about'),

    #Blog's pages
    path('pages/',              pages,          name='pages'),
    path('page/<id>',           page,           name='page'),
    path('new_page/',           new_page,       name='new_page'),
    path('edit_page/<id>',      edit_page,      name='edit_page'),
    path('delete_page/<id>',    delete_page,    name='delete_page'),

    path('login/',               login_request,    name='login'),
    path('register/',            register_request,    name='register'),
    path('logout/',              LogoutView.as_view(template_name="the_blog/logout.html"),    name='logout'),
    path('edit_user/',           edit_user,      name='edit_user'),
    path('create_avatar/',       create_avatar,      name='create_avatar'),
]
```


## Cuentas de usuario para iniciar sesion.

```bash
user: admin
pass: programacion2

user: admin2
pass: programacion3

user: c_angel
pass: anGel88c*
```



## Actividades
### Angel Carreon
- Creacion de modelos de Usuario y Blog
- CRUD de Blog.
- Estructura de las plantillas de HTML.
- Creacion de formularios e integracion con CKEditor
- Estilización de las vistas HTML mediante crisp
- Creación de modelos de AVATARES
- Creacion de Login, Logout y Registro

### Arely Torres
- Creacion del proyecto inicial
- Definir Estructura de archivos
- Seleccion e integración de plantillas