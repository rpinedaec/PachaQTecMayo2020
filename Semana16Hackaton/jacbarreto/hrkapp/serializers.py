from django.contrib.auth.models import User, Group
from .models import artista,album,cancion,tipomusica,catalogo,usuario,playlist
#Auto, Marca, Tipo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        #fields = ['url', 'name']
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = artista
        #fields = ['url', 'artista']
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = album
        #fields = ['url', 'album', 'artista']
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = cancion
        #fields = ['url', 'cancion','album']
        fields = '__all__'

class TipomusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipomusica
        #fields = ['url', 'tipomusica']   
        fields = '__all__'

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo
        #fields = ['url', 'catalogo','tipomusica','cancion']   
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        #fields = ['url', 'nombre']  
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = playlist
        #fields = ['url', 'playlist', 'catalogo','nombre']           
        fields = '__all__'

