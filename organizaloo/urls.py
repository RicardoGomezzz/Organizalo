from django.urls import path
from organizaloo.views import index,formulario, inicio, listado_trans, login,menu,registro, modificar_trans
from re import A



urlpatterns = [
    path('index/', index,name='index'),
    path('formulario/',formulario, name='Formulario'),
    path('inicio/',inicio, name='inicio'),
    path('login/',login, name='login'),
    path('',menu, name='menu'),
    path('registro/',registro, name='registro'),
    path('listado/',listado_trans, name='listado'),
    path('modificar/<id>/',modificar_trans, name='modificar'),


]