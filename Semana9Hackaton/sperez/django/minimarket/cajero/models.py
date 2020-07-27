from django.db import models
from almacen.models import Producto

# Create your models here.
TIPO_VENTA = [
    ('e','efectivo'),
    ('t','tarjeta')
]

class venta(models.Model):
    cliente = models.CharField(max_length=200)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_VENTA)
    cantidad =models.IntegerField(default=0)

class factura(models.Model):
    cliente = models.ForeignKey(venta, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    ruc_dni = models.BigIntegerField(verbose_name='ruc_dni')
    fecha = models.DateField()
    igv = models.DecimalField(max_digits=3, decimal_places=3)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    monto_pagar = models.DecimalField(max_digits=10, decimal_places=2)



