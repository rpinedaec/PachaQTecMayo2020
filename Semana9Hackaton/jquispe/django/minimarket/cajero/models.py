from django.db import models
from almacen.models import Producto
# Create your models here.

class Cliente(models.Model):
	nombreCliente = models.CharField(max_length=200)
	dniCliente = models.CharField(max_length=8)
	direccionCliente = models.CharField(max_length=200)

class Empresa(models.Model):
	rucEmpresa = models.CharField(max_length=11)
	direccionEmpresa = models.CharField(max_length=200)

class FacturaCabecera(models.Model):
	fechaFacturaCabecera = models.DateTimeField()
	igvFacturaCabecera = models.DecimalField(max_digits=10, decimal_places=2)
	subtotalFacturaCabecera = models.DecimalField(max_digits=10, decimal_places=2)
	totalFacturaCabecera = models.DecimalField(max_digits=10, decimal_places=2)
	estadoFactura = models.CharField(max_length=20)
	idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class facturaDetalle(models.Model):
	cantFactDetalle = models.IntegerField(default=0)
	valorFactDetalle = models.DecimalField(max_digits=10,decimal_places=2)
	idFacturaCabecera = models.ForeignKey(FacturaCabecera, on_delete=models.CASCADE)
	idProductos = models.ForeignKey(Producto, on_delete=models.CASCADE)