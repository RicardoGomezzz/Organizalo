from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):  #PAGINA 1
    return render(request, 'organizalo/base.html')

def formulario(request):
    return render (request, 'organizalo/formTransaccion.html')

def inicio(request): #PAGINA INICIO
    return render (request, 'organizalo/home.html')