from django.db import models

# Create your models here.

class tipoDocumento(models.Model):
    def __str__(self):
        return f"{self.Descripcion}"
    DNI = 'D'
    Libreta_Electoral = 'LE'    
    Pasaporte = 'P'
    Tipo = ((DNI,'DNI'),(Libreta_Electoral,'Libreta Electora'), (Pasaporte, 'Pasaporte'))
    Descripcion = models.CharField(
        max_length=2,
        choices=Tipo,
        default=DNI,
    )

class Producto(models.Model):
    SI = 'S'
    NO = 'N'
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    desigv = ((SI, 'Si'), (NO, 'No'))
    igv = models.CharField(
        max_length = 2,
        choices = desigv,
        default = SI,
    ) 

class Tecnico(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    numeroDocumento = models.CharField(max_length=15)

class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    numeroDocumento = models.CharField(max_length=15)

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

class detalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
