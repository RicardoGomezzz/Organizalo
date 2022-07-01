from django.urls import path
from organizaloo.views import index,formulario
from re import A



urlpatterns = [
    path('index/', index,name='index'),
    path('formulario/',formulario, name='Formulario')
]