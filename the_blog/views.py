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


