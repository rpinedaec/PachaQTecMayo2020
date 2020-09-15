from django.db import models

# Create your models here.
class artista(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    nombre = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=200)

class album(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    nombre = models.CharField(max_length=200)

class cancion(models.Model):
    def __str__(self):
        return f"{self.nombre}, {self.artista}, {self.album}"
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    artista = models.ForeignKey(artista, on_delete=models.CASCADE)
    album = models.ForeignKey(album, on_delete=models.CASCADE)

class user(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)

class playlist(models.Model):
    def __str__(self):
        return f"{self.nombre}, {self.user}"
    nombre = models.CharField(max_length=200)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

class canciondeplaylist(models.Model):
    def __str__(self):
        return f"{self.cancion}, {self.playlist}"
    cancion = models.ForeignKey(cancion, on_delete=models.CASCADE)
    playlist = models.ForeignKey(playlist, on_delete=models.CASCADE)