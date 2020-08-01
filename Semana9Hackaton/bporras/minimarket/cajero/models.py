from django.db import models
from almacen.models import Producto
from administrador.models import Administrador
# Create your models here.
class Cajero(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)

class FacturaCabecera(models.Model):
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codCajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    codAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    fechaFact = models.DateTimeField(auto_now_add=True, auto_now=False)

class FacturaDetalle(models.Model):
    codFacCabecera = models.ForeignKey(FacturaCabecera, on_delete=models.CASCADE)
    codProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadProducto = models.DecimalField(default=0,max_digits=10, decimal_places=2)