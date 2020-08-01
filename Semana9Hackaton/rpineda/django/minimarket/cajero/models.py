from django.db import models
from almacen.models import Producto

# Create your models here.
class Metodo_pago(models.Model):
    descripcione = models.CharField(max_length=200)

class Detalle_factura(models.Model):
    fecha= models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad =models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    IGV= models.DecimalField(max_digits=10, decimal_places=2)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

class Factura(models.Model):
    id_detalle_factura= models.ForeignKey(Detalle_factura, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    IGV= models.DecimalField(max_digits=10, decimal_places=2)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.ForeignKey(Metodo_pago, on_delete=models.CASCADE)