from django.db import models

# Create your models here.
class Administrador(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Documento = models.IntegerField(default=0)