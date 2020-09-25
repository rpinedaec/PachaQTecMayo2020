from django.db import models

# Create your models here.

class Song(models.Model):

    musicname = models.CharField(max_length=50)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)
    idSinger = models.ForeignKey(Singer, on_delete = models.CASCADE)

    def __str__(self):

        return f"{self.musicname}, {self.genero}, {self.anio}"

class Singer(models.Model):

    namesinger = models.CharField(max_length=50)

    def __str__(self):

        return f"{self.namesinger}"

class Albun(models.Model):

    namealbun = models.CharField(max_length=50)
    idSong = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.descripcion}"

class Playlist(models.Model):

    descripcion = models.CharField(max_length=50)
    idAlbum = models.ForeignKey(Albun, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.descripcion}"

class User(models.Model):

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idPlaylist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.name},{self.lastname}"
