from django.db import models
from django.utils import timezone

# Create your models here.

class tipo(models.Model):

    descripcion = models.CharField(max_length=100)

    def __str__(self):

        return f"{self.descripcion}"

class marca(models.Model):
    
    descripcion = models.CharField(max_length=100)
    modelo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.descripcion},{self.modelo}"

class vehiculo(models.Model):
	
    tipo = models.ForeignKey('tipo',on_delete=models.CASCADE)
    marca = models.ForeignKey('marca',on_delete=models.CASCADE)
    numero_serie = models.CharField(max_length = 80)
    precio = models.FloatField()
    
    def __str__(self):
        
        return f"{self.tipo},{self.marca},{self.precio}"
