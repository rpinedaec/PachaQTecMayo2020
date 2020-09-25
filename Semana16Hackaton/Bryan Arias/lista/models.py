from django.db import models
from lista.managers import ArtistaManager, AlbumManager

# Create your models here.
class Artista(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Celular = models.CharField(max_length=15)
    Correo = models.CharField(max_length=100)

    objects = ArtistaManager()

    def __str__(self):
        return self.Nombre

class Album(models.Model):
    Artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Fecha_Lanzamiento = models.DateField()

    objects = AlbumManager()

    def __str__(self):
        return self.Nombre

class Cancion(models.Model):
    Artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.Nombre

class Usuario(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Celular = models.CharField(max_length=15)
    Correo = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre

class Playlist(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.Descripcion

class CancionPlaylist(models.Model):
    Playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)    
    Cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
