from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def Listado_usuarios (request): 
    return render (request, 'listado.html')
    


class FormularioTransaccionView(HttpRequest):
    
    def index(request):
        data = {'form': FormularioTransaccion()}
        return render(request,"template/index.html", data)
    
        if request.method == 'POST':
            formulario = FormularioTransaccion(data=request.POST)
            if FormularioTransaccion.is_valid():
                FormularioTransaccion.save()
                data["Mensaje"] = "Datos Registrados"
            else:
                data["form"] = FormularioTransaccion
    
    def procesar_formulario(request):
        transaccion = FormularioTransaccion(request.POST)
        if transaccion.is_valid():
            transaccion.save()
            transaccion - FormularioTransaccion()
            
        return render(request,"TransaccionIndex.html", {"form":transaccion, "mensaje": 'OK'})
    
    

        