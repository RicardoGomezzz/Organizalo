
from django.db import models

# Create your models here.


class Descripcion(models.Model):
    nombre = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre
    
class Monto(models.Model):
    cantidad = models.IntegerField()

class Cuenta(models.Model):
    tipo= models.CharField(max_length=50)

    
    


    
