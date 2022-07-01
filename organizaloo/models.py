from django.db import models

# Create your models here.


opciones_cuenta = [
    
    [0, 'Debito'],
    [1, 'Visa'],
    [2, 'Mach'],
    [3, 'Efectivo']
    
]



class Transaccion(models.Model):
    Fecha = models.DateField()
    Descripcion = models.CharField(max_length=150)
    Monto = models.IntegerField()
    Cuenta = models.IntegerField(choices=opciones_cuenta)
    
    def __str__(self):
        return self.Descripcion
    