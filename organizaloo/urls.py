from django.urls import path
<<<<<<< HEAD
from organizaloo.views import index,formulario, inicio, listado_trans, login,menu,registro, modificar_trans
=======
from organizaloo.views import index,formulario, inicio, listado_trans, login,menu,registro,eliminar_dato
>>>>>>> 10eb33cc356900710c74d20c696139485daad138
from re import A



urlpatterns = [
    path('index/', index,name='index'),
    path('formulario/',formulario, name='Formulario'),
    path('inicio/',inicio, name='inicio'),
    path('login/',login, name='login'),
    path('',menu, name='menu'),
    path('registro/',registro, name='registro'),
    path('listado/',listado_trans, name='listado'),
<<<<<<< HEAD
    path('modificar/<id>/',modificar_trans, name='modificar'),
=======
    path('eliminar/<id>/',eliminar_dato, name='eliminar')
>>>>>>> 10eb33cc356900710c74d20c696139485daad138


]