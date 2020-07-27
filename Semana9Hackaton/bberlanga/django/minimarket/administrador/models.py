from django.db import models
from almacen.models import Producto
from cajero.models import Factura

# Create your models here.
class Periodo(models.Model):
    fecha_apertura=models.DateField()
    fecha_cierre=models.DateField()

class Transaccion(models.Model):
     descripcion=models.CharField(max_length=30)

class Consolidado_actividades(models.Model):
    id_periodo=models.ForeignKey(Periodo,on_delete=models.CASCADE)
    id_transsaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    id_factura=models.ForeignKey(Factura, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    IGV= models.DecimalField(max_digits=10, decimal_places=2)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
