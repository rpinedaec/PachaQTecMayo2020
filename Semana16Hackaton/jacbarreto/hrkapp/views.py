#from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets 
#, permissions
from hrkapp.serializers import UserSerializer, GroupSerializer, ArtistaSerializer, AlbumSerializer, CancionSerializer, TipomusicaSerializer, CatalogoSerializer, UsuarioSerializer, PlaylistSerializer
from hrkapp.models import artista, album, cancion, tipomusica, catalogo, usuario, playlist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = artista.objects.all()
    serializer_class = ArtistaSerializer
    #permission_classes =  [permissions.IsAuthenticated]
    
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = album.objects.all()
    serializer_class = AlbumSerializer
    #permission_classes =  [permissions.IsAuthenticated]

class CancionViewSet(viewsets.ModelViewSet):
    queryset = cancion.objects.all()
    serializer_class = CancionSerializer
    #permission_classes = [permissions.IsAuthenticated]

class TipomusicaViewSet(viewsets.ModelViewSet):
    queryset = tipomusica.objects.all()
    serializer_class = TipomusicaSerializer
    #permission_classes = [permissions.IsAuthenticated]    

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = catalogo.objects.all()
    serializer_class = CatalogoSerializer
    #permission_classes = [permissions.IsAuthenticated]       

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]        

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = playlist.objects.all()
    serializer_class = PlaylistSerializer
    #permission_classes = [permissions.IsAuthenticated]     