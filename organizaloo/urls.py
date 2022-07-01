from django.urls import path
from organizaloo.views import index,formulario, inicio, login,menu,registro, listado
from re import A



urlpatterns = [
    path('index/', index,name='index'),
    path('formulario/',formulario, name='Formulario'),
    path('inicio/',inicio, name='inicio'),
    path('login/',login, name='login'),
    path('menu/',menu, name='menu'),
    path('registro/',registro, name='registro'),
    path('listado/',listado, name='listado'),


]