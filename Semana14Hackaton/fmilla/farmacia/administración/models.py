from django.db import models

# Create your models here.
class tipoProducto(models.Model):
    def __str__(self):
        return f"{self.descripcion}, {self.isActivo}"
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class producto(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    nombre = models.CharField(max_length=200)
    tipoproducto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)
    igv = models.BooleanField()
    costo = models.DecimalField(max_digits=10,decimal_places=2)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class tipoCliente(models.Model):
    def __str__(self):
        return f"{self.descripcion}, {self.isActivo}"
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class tipoDocumento(models.Model):
    def __str__(self):
        return f"{self.descripcion}, {self.isActivo}"
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class cliente(models.Model):
    ACTIVO = 'AC'
    INACTIVO = 'IA'
    tipocliente = models.ForeignKey(tipoCliente,on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.CharField(max_length=15)
    direccion = models.TextField(max_length=1000, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    isActivo = models.CharField(
        max_length=2,
        choices=isActivoEnum,
        default=ACTIVO,
    )

class pedido(models.Model):
    cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    ubicacion = models.CharField(max_length=500, null= True)
    estado = models.CharField(max_length=30,default='Recibido')

class detallePedido(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()