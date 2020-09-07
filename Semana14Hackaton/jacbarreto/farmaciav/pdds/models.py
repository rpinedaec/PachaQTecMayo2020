from django.db import models

# Create your models here.
class tipoCliente(models.Model):
    def __str__(self):
    #    return f"{self.descripcion}, {self.isActivo}"
        return f"{self.descripcion}"
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
    #     #return f"{self.descripcion}, {self.isActivo}"
        return f"{self.descripcion}"
    # ACTIVO = 'AC'
    # INACTIVO = 'IA'
    descripcion = models.CharField(max_length=200)
    # isActivoEnum = ((ACTIVO,'Activo'),(INACTIVO,'Inactivo'))
    # isActivo = models.CharField(
    #     max_length=2,
    #     choices=isActivoEnum,
    #     default=ACTIVO,
    # )

class cliente(models.Model):
    tipocliente = models.ForeignKey(tipoCliente,on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.IntegerField(max_length=15)
    direccion = models.TextField(max_length=1000, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    puntos = models.IntegerField(max_length=8)

# class TipoDocumento(models.Model):
#     descripcion = models.CharField(max_length=45)
class vendedor(models.Model):
    dni = models.IntegerField(max_length=8)
    codigo = models.IntegerField(max_length=8)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

class uMedida(models.Model):
    sigla = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=200)

class categoria(models.Model):
    descripcion = models.CharField(max_length=200)

class tipoProducto(models.Model):
    descripcion = models.CharField(max_length=200)

class producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.BooleanField()
    presentacion = models.CharField(max_length=200)
    fechavenc = models.DateTimeField()
    existenciainic = models.IntegerField(max_length=8)
    entradas = models.IntegerField(max_length=8)
    salidas = models.IntegerField(max_length=8)
    stock = models.IntegerField(default=0)
    umedida = models.ForeignKey(uMedida, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    tipoproducto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)

class pedido(models.Model):
    cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    #transportista = models.ForeignKey(transportista, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(vendedor,on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    #ubicacion = models.CharField(max_length=500, null= True)
    #estado = models.CharField(max_length=30,default='Recibido')

class detallePedido(models.Model):
    pedido = models.ForeignKey(pedido,on_delete=models.CASCADE)
    producto = models.ForeignKey(producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)





