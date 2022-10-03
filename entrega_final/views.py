from django.http import HttpResponse

def saludar(request):
    return  HttpResponse('Hola a todos')