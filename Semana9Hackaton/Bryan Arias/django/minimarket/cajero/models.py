from django.db import models
from datetime import datetime
from almacen.models import Producto

# Create your models here.
class Documento(models.Model):
    Descripcion = models.CharField(max_length=25)

class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    Factura = models.ManyToManyField(Producto, through='Factura')
    Tipo_Documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    Numero_Documento = models.CharField(max_length=10)

class Factura(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(default=0)
    Fecha = models.DateTimeField(default=datetime.now)