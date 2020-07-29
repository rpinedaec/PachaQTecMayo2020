from django.db import models
from almacen.models import Producto

# Create your models here.
class FacturaVenta(models.Model):
    nombreCliente = models.CharField(max_length=200)
    fechaFact = models.DateTimeField(auto_now_add=True, auto_now=False)
    producto = models.CharField(max_length=200, default='')
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)



#models.CharField
