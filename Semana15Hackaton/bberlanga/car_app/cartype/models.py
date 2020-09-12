from django.db import models
from django.utils import timezone


options= ((1,'automatic'),(2,'mecanic'))

class CarType(models.Model):
    description = models.CharField(max_length=20)
    system = models.CharField(max_length=20, choices=options)
    updated = models.DateTimeField(default=timezone.now)



