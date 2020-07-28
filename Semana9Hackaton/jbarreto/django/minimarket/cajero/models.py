from django.db import models
#from minimarket.almacen.models import Producto
from almacen.models import Producto

# Create your models here.
class Cliente(models.Model):
    Dni = models.IntegerField(max_length=8)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

class Cab_comprobantepago(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tipodoc = models.CharField(max_length=1)
    nro_tipodoc = models.CharField(max_length=8)
    igv = models.FloatField(default=0.18)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente,  on_delete = models.CASCADE)

class Det_comprobantepago(models.Model):
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    cabcomprobantepago = models.ForeignKey(Cab_comprobantepago, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    