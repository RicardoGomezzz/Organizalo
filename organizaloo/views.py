import imp
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):  #PAGINA 1
    return render(request, 'organizalo/base.html')


def form(request):  #PAGINA 1
    return render(request, 'organizalo/formTransaccion.html')
