from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Transaccion
from .forms import TransaccionForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
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
            data["mensaje"]="Datos Guardados!"
        else:
            data["form"] = formulario
    return render (request, 'organizalo/formTransaccion.html',data)

def inicio(request): #PAGINA INICIO
    return render (request, 'organizalo/home.html')

def login(request): #PAGINA INICIO
    return render (request, 'organizalo/registration/login.html')

def menu(request): #PAGINA INICIO
    return render (request, 'organizalo/menu.html')


def listado_trans(request): #LISTA DE MOVIMIENTOS
    listado = Transaccion.objects.all();
    return render (request, 'organizalo/Listado.html', {'listado': listado})


def modificar_trans(request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    
    data = {
        
        'form': TransaccionForm(instance=transaccion)
        
    }
    
    if request.method == 'POST':
        formulario = TransaccionForm(data=request.POST, instance=transaccion)
        if formulario.is_valid():
            formulario.save()
            #messages.success(request, "Modificado Correctamente!")
            return redirect(to="listado")
        data['form'] = formulario
    
    return render(request, 'organizalo/modificar.html', data)

def eliminar_dato (request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    transaccion.delete()
    
    return redirect (to='listado')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.succes(request, f'Usuario {username} creado con exito')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}        
    return render(request, 'organizalo/registration/registro.html', context)



def pagapi(request): #PAGINA INICIO
    return render (request, 'organizalo/apidolar.html')