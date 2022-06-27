
from django.db import models

# Create your models here.


class Descripcion(models.model):
    Descripcionn = models.CharField(max_length=300)
    Descripcionn = models.ForeignKey(Monto, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.Descripcionn
    
class Monto(models.Model):
    Cantidad = models.IntegerField(max_length=10)

class Cuenta(models.Model):
    Tipo= models.CharField(max_length=50)

    
    


    
