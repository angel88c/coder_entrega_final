from django.urls import path
from the_blog.views import *

from django.contrib.auth.views import LogoutView

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

]