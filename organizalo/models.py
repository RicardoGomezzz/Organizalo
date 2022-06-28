
from django.db import models

# Create your models here.



tipos_cuenta = {
    
    [0, "Debito Banco Estado"],
    [1, "Visa"],
    [2, "Mach"],
    [3, "Efectivo"]
}



class Transaccion(models.Model):
    Descripcion = models.CharField(max_length=300)
    Monto = models.IntegerField()
    Cuenta = models.IntegerField(choices=tipos_cuenta)
    codigo = models.ForeignKey(Transaccion, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.Monto
    


    
    


    
