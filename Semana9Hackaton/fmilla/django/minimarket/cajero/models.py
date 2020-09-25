from django.db import models
from almacen.models import Producto
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    nroIdentificacion = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    tipoPago = models.CharField(max_length=200,default='credito')
    fecha = models.DateField(auto_now = True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    producto_comprado = models.ForeignKey(Producto, on_delete=models.CASCADE)