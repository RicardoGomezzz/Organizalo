from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Transaccion
from .forms import TransaccionForm
from django.contrib import messages
# Create your views here.

def index(request):  #PAGINA 1
    return render(request, 'organizalo/base.html')

def formulario(request):
    data = {
        'form': TransaccionForm()
    }
    if request.method == 'POST':
        formulario = TransaccionForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="mensaje enviado"
        else:
            data["form"] = formulario
    return render (request, 'organizalo/formTransaccion.html',data)

def inicio(request): #PAGINA INICIO
    return render (request, 'organizalo/home.html')

def login(request): #PAGINA INICIO
    return render (request, 'organizalo/login.html')

def menu(request): #PAGINA INICIO
    return render (request, 'organizalo/menu.html')

def registro(request): #PAGINA INICIO
    return render (request, 'organizalo/registro.html')

def listado_trans(request): #LISTA DE MOVIMIENTOS
    listado = Transaccion.objects.all();
    return render (request, 'organizalo/Listado.html', {'listado': listado})


def modificar_trans(request, id):
    
    return render(request, 'organizalo/modificar.html')

def eliminar_dato (request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    transaccion.delete()
    
    return redirect (to='listado')
