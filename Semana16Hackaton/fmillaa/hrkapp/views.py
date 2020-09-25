from django.shortcuts import render
# from rest_framework import permissions
from hrkapp.serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer, UserSerializer, PlaylistSerializer, CancionDePlaylistSerializer
from hrkapp.models import artista, album, cancion, user, playlist, canciondeplaylist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre']

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre']

class CancionViewSet(viewsets.ModelViewSet):
    queryset = cancion.objects.all()
    serializer_class = CancionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    raw_id_fields = ('artista','album')
    search_fields=['nombre','genero','artista__nombre','album__nombre']

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre','correo']

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    raw_id_fields = ('user')
    search_fields=['nombre','user__nombre']

class CancionDePlaylistViewSet(viewsets.ModelViewSet):
    queryset = canciondeplaylist.objects.all()
    serializer_class = CancionDePlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    raw_id_fields = ('cancion','playlist')
    search_fields=['cancion__nombre','playlist__nombre']
