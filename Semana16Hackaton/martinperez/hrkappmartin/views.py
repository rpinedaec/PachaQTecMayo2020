from rest_framework import viewsets
from hrkappmartin.serializers import PeliculaSerializer,ArtistaSerializer,CancionSerializer,AlbumSerializer,PlaylistSerializer
from hrkappmartin.models import Pelicula,artista,cancion,album,playlist
  

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = artista.objects.all()
    serializer_class = ArtistaSerializer

class CancionViewSet(viewsets.ModelViewSet):
    queryset = cancion.objects.all()
    serializer_class = CancionSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = album.objects.all()
    serializer_class = AlbumSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = playlist.objects.all()
    serializer_class = PlaylistSerializer

