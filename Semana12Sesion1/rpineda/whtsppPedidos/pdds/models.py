from django.db import models

# Create your models here.
class tipoClientes(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class tipoDocumentos(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )
class tipoProductos(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )