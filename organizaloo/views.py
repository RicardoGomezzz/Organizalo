from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaccion
# Create your views here.

def index(request):  #PAGINA 1
    return render(request, 'organizalo/base.html')

def formulario(request):
    return render (request, 'organizalo/formTransaccion.html')

def inicio(request): #PAGINA INICIO
    return render (request, 'organizalo/home.html')

def login(request): #PAGINA INICIO
    return render (request, 'organizalo/login.html')

def menu(request): #PAGINA INICIO
    return render (request, 'organizalo/menu.html')

def registro(request): #PAGINA INICIO
    return render (request, 'organizalo/registro.html')

def listado(request): #LISTA DE MOVIMIENTOS
    transaccion = Transaccion.objects.all()
    data = {
        'transacciones': transaccion
        
    }
    return render (request, 'organizalo/Listado.html')