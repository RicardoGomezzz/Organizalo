from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bievenida(request):
    return HttpResponse("Bienvenidos a la pagina web")
