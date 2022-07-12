from django.contrib import admin
from .models import Transaccion, Contacto
# Register your models here.


class TransaccionAdmin(admin.ModelAdmin):
    list_display = ["Fecha", "Descripcion", "Monto", "Cuenta"]
    list_editable = ["Monto"]
    search_fields = ["Descripcion"]
    list_filter = ["Descripcion", "Monto"]
    list_per_page = 5


admin.site.register(Transaccion)
admin.site.register(Contacto)