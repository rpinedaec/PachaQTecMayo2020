from market.models import Productos
from django.utils import timezone
from django.db import models
# Create your models here.


class Clientes (models.Model):
    nombre = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)


class Factura (models.Model):
    fechaCreacion = models.DateTimeField(default=timezone.now)
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    montoTotal = models.FloatField(default=0)


class FacturasProductos(models.Model):  # many to many
    fechaCreacion = models.DateTimeField(default=timezone.now)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
