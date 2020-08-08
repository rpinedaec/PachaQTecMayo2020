from django.db import models
from almacen.models import Producto
from administrador.models import Administrador

# Create your models here.
class Cajero(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    ID = models.IntegerField(default=0)

class Cliente(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Documento = models.IntegerField(default=0)

class FacturaCabecera(models.Model):
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codCajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    codAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    Subtotal = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    Total = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    fechaFact = models.DateTimeField(auto_now_add=True, auto_now=False)

class FacturaDetalle(models.Model):
    codFacCabecera = models.ForeignKey(FacturaCabecera, on_delete=models.CASCADE)
    codProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadProducto = models.DecimalField(default=0,max_digits=10, decimal_places=2)