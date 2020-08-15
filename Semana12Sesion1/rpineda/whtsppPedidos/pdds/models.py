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

class transportistas(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    tipoDocumento = models.ForeignKey(tipoDocumentos, on_delete=models.CASCADE)
    documento = models.CharField(max_length=15)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class productos(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    nombre = models.CharField(max_length=200)
    tipoproducto = models.ForeignKey(tipoProductos, on_delete=models.CASCADE)
    igv = models.BooleanField()
    costo = models.DecimalField(max_digits=10,decimal_places=2)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class clientes(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    tipocliente = models.ForeignKey(tipoClientes,on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(tipoDocumentos, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    docmento = models.CharField(max_length=15)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class pedidos(models.Model):
    cliente = models.ForeignKey(tipoClientes,on_delete=models.CASCADE)
    transportista = models.ForeignKey(transportistas, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    ubicacion = models.CharField(max_length=500)

class detallePedido(models.Model):
    pedido = models.ForeignKey(pedidos, on_delete=models.CASCADE)
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
