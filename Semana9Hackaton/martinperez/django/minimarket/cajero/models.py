from django.db import models
from almacen.models import Producto

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    ruc = models.IntegerField(default=99999999999)
    direccion = models.CharField(max_length=200)
    def __str__(self): 
        return self.nombre

class Compras(models.Model):
    Correlativo = models.IntegerField(default=0)
    fecha = models.DateField() 
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL,blank=True,null=True)
    precio = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    cantidad = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    def __str__(self): 
        return 'F001-000'+str(self.Correlativo)
 
