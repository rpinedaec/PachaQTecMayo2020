from django.db import models
 
class Pelicula(models.Model):
    code = models.CharField( max_length=10)
    name = models.CharField( max_length=50)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    mes = models.IntegerField()

    def __str__(self):
        return self.code

 

class artista(models.Model):
    class Meta:
        db_table = 'artista'    
    def __str__(self):
        return f"{self.nombre}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    nombre = models.CharField( max_length=200, blank=True, null=True)
    apellidos = models.CharField( max_length=200, blank=True, null=True)
    direccion = models.CharField( max_length=200, blank=True, null=True)
    telefono = models.IntegerField()
    email = models.CharField( max_length=200, blank=True, null=True)
    actividadPrincipal = models.CharField( max_length=200, blank=True, null=True)
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # cancion = models.ForeignKey(cancion, on_delete=models.CASCADE,default=1)
    # artista_cancion = models.ForeignKey(artista_cancion, on_delete=models.CASCADE,default=1)
    

class cancion(models.Model):
    class Meta:
        db_table = 'cancion'
    def __str__(self):
        return f"{self.descripcion}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    descripcion = models.CharField( max_length=200, blank=True, null=True)
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False) 
    artista = models.ForeignKey(artista, on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 
 


class album(models.Model):
    class Meta:
        db_table = 'album'
    def __str__(self):
        return f"{self.descripcion}, {self.descripcion}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    descripcion = models.CharField( max_length=200, blank=True, null=True)
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 
    cancion = models.ForeignKey(cancion, on_delete=models.CASCADE, default=1)
 


class playlist(models.Model):
    class Meta:
        db_table = 'playlist'
    def __str__(self):
        return f"{self.descripcion}"
    CHOICE = [(True,'ACTIVO'),(False,'INACTIVO')]  
    descripcion = models.CharField( max_length=200, blank=True, null=True)
    activo = models.BooleanField(choices=CHOICE,default=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 
    cancion = models.ForeignKey(cancion, on_delete=models.CASCADE, default=1)
 
