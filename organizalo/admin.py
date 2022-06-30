from django.contrib import admin
from .models import Transaccion
# Register your models here.




class TransaccionAdmin(admin.ModelAdmin):
    list = ('Descripcion','Monto','Cuenta','codigo')
    admin.site.register(Transaccion)
    
