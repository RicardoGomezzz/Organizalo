from django.shortcuts import render
from django.http import HttpRequest

from organizalo.forms import FormularioTransaccion

# Create your views here.

class FormularioTransaccionView(HttpRequest):
    
    def index(request):
        transaccion = FormularioTransaccion()
        return render(request,"TransaccionIndex.html", {"form":transaccion})
    
    def procesar_formulario(request):
        transaccion = FormularioTransaccion()
        if transaccion.is_valid():
            transaccion.save()
            transaccion - FormularioTransaccion()
            
        return render(request,"TransaccionIndex.html", {"form":transaccion, "mensaje": 'OK'})
    
    

        