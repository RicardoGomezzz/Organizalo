from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
    
    
def bienvenida(request):
    return HttpResponse("Hola mundo!")

        