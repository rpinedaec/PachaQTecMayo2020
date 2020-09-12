from django.db import models
from django.utils import timezone


class Brand(models.Model):
    description=models.CharField(max_length=200, null=False)
    updated = models.DateTimeField(default=timezone.now)
