"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from organizalo.views import bienvenida
=======
<<<<<<< HEAD
=======
from organizalo.views import formu
>>>>>>> 0d19faf1284f0fe4d4aabca90e2c4e7d946dbefb
>>>>>>> 49c70ae28d89b0f790fe0d0594e7e07579148d1f



urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('bienvenida/', bienvenida)
=======
<<<<<<< HEAD
    path('registrarTransaccion/', FormularioTransaccionView.index, name='registrarTransaccion'),
=======
    path('', formu, name="Index")  ,
    path('registrarTransaccion/', FormularioTransaccionView.formu, name='registrarTransaccion'),
>>>>>>> 0d19faf1284f0fe4d4aabca90e2c4e7d946dbefb
    path('guardarTransaccion/', FormularioTransaccionView.procesar_formulario, name='guardarTransaccion')
>>>>>>> 49c70ae28d89b0f790fe0d0594e7e07579148d1f
]
