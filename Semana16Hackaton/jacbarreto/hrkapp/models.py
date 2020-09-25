from django.db import models

# Create your models here.
class artista(models.Model):
    artista = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.code

class album(models.Model):
    album = models.CharField(max_length=200)
    artista = models.ForeignKey(artista, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.code

class cancion(models.Model):
    cancion = models.CharField(max_length=200)
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.code

class tipomusica(models.Model):
    tipomusica = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.code

class catalogo(models.Model):
    catalogo = models.CharField(max_length=200)
    tipomusica = models.ForeignKey(tipomusica, on_delete=models.CASCADE)
    cancion = models.ForeignKey(cancion, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.code

class usuario(models.Model):           
    nombre = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.code

class playlist(models.Model):
    playlist = models.CharField(max_length=200)
    catalogo = models.ForeignKey(catalogo, on_delete=models.CASCADE)
    nombre =  models.ForeignKey(usuario, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.code