from django.db import models

# Create your models here.

class Artista(models.Model):
    name = models.CharField( max_length=50)
    is_favorite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name= 'artista'
        verbose_name_plural=  'artistas'
    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artista, on_delete=models.CASCADE)
    title = models.IntegerField()
    genre = models.DateTimeField(auto_now_add=True)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name= 'album'
        verbose_name_plural=  'albumes'
    def __str__(self):
        return self.title + '-' + self.artist

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name= 'cancion'
        verbose_name_plural=  'canciones'

    def __str__(self):
        return self.song_title

class Usuarios(models.Model):
    name = models.CharField( max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    code = models.CharField( max_length=10)
    name = models.CharField( max_length=50)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
