from django.urls import path
from organizaloo.views import index,formulario, inicio
from re import A



urlpatterns = [
    path('index/', index,name='index'),
    path('formulario/',formulario, name='Formulario'),
    path('inicio/',inicio, name='inicio'),
]