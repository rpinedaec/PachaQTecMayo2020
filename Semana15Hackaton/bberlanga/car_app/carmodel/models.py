from django.db import models
from django.db import models
from django.utils import timezone

options= ((1,'standard'),(2,'full'))

class CarModel(models.Model):
    description = models.CharField(max_length=20)
    interior = models.CharField(max_length=20, choices=options)
    updated = models.DateTimeField(default=timezone.now)
