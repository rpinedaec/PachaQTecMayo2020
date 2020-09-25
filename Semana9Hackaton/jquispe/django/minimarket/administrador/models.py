from django.db import models

# Create your models here.

class VentaDiaria(models.Model):
    venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()