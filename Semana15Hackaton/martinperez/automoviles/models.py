from django.db import models



class marca(models.Model):
    class Meta:
        db_table = 'marca'    
    def __str__(self):
        return f"{self.descripcion}, {self.activo}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    descripcion = models.CharField(max_length=200) 
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False)


class tipo(models.Model):
    class Meta:
        db_table = 'tipo'    
    def __str__(self):
        return f"{self.descripcion}, {self.activo}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    descripcion = models.CharField(max_length=200) 
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False)

class automovil(models.Model):
    class Meta:
        db_table = 'automovil'    
    def __str__(self):
        return f"{self.descripcion}, {self.activo}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    descripcion = models.CharField(max_length=200) 
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False)

