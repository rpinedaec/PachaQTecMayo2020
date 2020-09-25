from time import strptime

from django.db import models


class ArtistaManager(models.Manager):

    def get_artista_by_created(self, my_date):
        queryset = self.get_queryset()
        return queryset.all()

class AlbumManager(models.Manager):

    def get_album_by_created(self, my_date):
        queryset = self.get_queryset()
        return queryset.all()