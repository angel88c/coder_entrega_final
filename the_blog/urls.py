from django.urls import path
from the_blog.views import *

urlpatterns = [
    path('',                inicio,         name='inicio'),
    path('about/',          about,          name='about'),

    #Blog's pages
    path('pages/',          pages,          name='pages'),
    path('page/<id>',       page,           name='page'),
    path('new_page/',       new_page,       name='new_page'),
    path('edit_page/<id>',      edit_page,      name='edit_page'),
    path('delete_page/<id>',    delete_page,    name='delete_page'),

    ##Users
    #path('users/',           users,         name='users'),
    #path('new_user/',        new_user,      name='new_user'),
    #path('edit_user/<id>',   edit_user,     name='edit_user'),
    #path('delete_user/<id>', delete_user,   name='delete_user'),

    ##Signup and login
    #path('login',           login_request,  name='login'),
    #path('signup/',         signup,         name='signup'),
    
]