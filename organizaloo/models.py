from django.db import models

# Create your models here.


opciones_cuenta = [
    
    [0, "Debito"],
    [1, "Visa"],
    [2, "Mach"],
    [3, "Efectivo"]
    
]

opciones_consultas = [
    
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    
]



class Transaccion(models.Model):
    Fecha = models.DateField()
    Descripcion = models.CharField(max_length=150)
    Monto = models.IntegerField()
    Cuenta = models.IntegerField(choices=opciones_cuenta)
    
    def __str__(self):
        return self.Descripcion
    
class Contacto(models.Model):
    Nombre = models.CharField(max_length=50)
    Correo = models.EmailField()
    Tipo_consulta = models.IntegerField(choices=opciones_consultas)
    Mensaje = models.TextField()
    
def __str__(self):
    return self.Nombre

    