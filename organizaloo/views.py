from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Transaccion
from .forms import CustomUserCreationForm, TransaccionForm, ContactoForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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

def registro (request):
    data = {
        'form': CustomUserCreationForm()

    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Has completado el registro")
            return redirect(to="inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def pagapi(request): #PAGINA INICIO
    return render (request, 'organizalo/apidolar.html')

def contacto(request):
    data = { 
            'form': ContactoForm() 
            }
    if request.method == 'POST':
        formulario = ContactoForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Datos Guardados!"
        else:
            data["form"] = formulario
    return render(request, 'organizalo/contacto.html', data)