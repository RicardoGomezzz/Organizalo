from django.contrib import admin
from .models import Descripcion,Monto,Cuenta
# Register your models here.

class DescripcionAdmin(admin.ModelAdmin):
    list = ('nombre')
    admin.site.register(Descripcion)
    
class MontoAdmin(admin.ModelAdmin):
    list = ('cantidad')
    admin.site.register(Monto)

class CuentaAdmin(admin.ModelAdmin):
    list = ('tipo')
    admin.site.register(Cuenta)