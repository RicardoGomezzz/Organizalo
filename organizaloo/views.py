from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bievenida(request):
    return render (HttpResponse("Bienvenidos a la pagina web"))
