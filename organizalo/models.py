
from django.db import models

# Create your models here.



<<<<<<< HEAD
tipos_cuenta = [
    
=======
tipos_cuenta = [ 
                    
>>>>>>> 0d19faf1284f0fe4d4aabca90e2c4e7d946dbefb
    [0, "Debito Banco Estado"],
    [1, "Visa"],
    [2, "Mach"],
    [3, "Efectivo"]
<<<<<<< HEAD
]


class Code(models.Model):
    nro = models.IntegerField() 
=======
    ]
>>>>>>> 0d19faf1284f0fe4d4aabca90e2c4e7d946dbefb



class Transaccion(models.Model):
    Descripcion = models.CharField(max_length=300)
    Monto = models.IntegerField()
    Cuenta = models.IntegerField(choices=tipos_cuenta)
<<<<<<< HEAD
    codigo = models.ForeignKey(Code, on_delete=models.DO_NOTHING)
=======
>>>>>>> 0d19faf1284f0fe4d4aabca90e2c4e7d946dbefb
    
    def __str__(self):
        return self.Monto
    


    
    


    
