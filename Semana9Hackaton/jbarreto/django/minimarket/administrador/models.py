from django.db import models
#from minimarket.cajero.models import Cab_comprobantepago
from cajero.models import Cab_comprobantepago

# Create your models here.
class ReporteVentas(models.Model):
    fechareporte = models.DateTimeField(auto_now_add=True)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cabcomprobantepago = models.ForeignKey(Cab_comprobantepago, on_delete = models.CASCADE)
    