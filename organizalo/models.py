
from django.db import models

# Create your models here.


class Transaccion(models.Model):
    Descripcion = models.CharField(max_length=300)
    Monto = models.IntegerField()
    Cuenta = models.CharField(max_length=50)
    codigo = models.IntegerField()
    


    
    


    
