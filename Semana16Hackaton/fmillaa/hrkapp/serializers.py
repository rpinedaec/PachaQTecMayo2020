from .models import artista, album, cancion, user, playlist, canciondeplaylist
from rest_framework import serializers

class ArtistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artista
        fields = ['nombre','nacionalidad']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = album
        fields = ['nombre']

class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cancion
        fields = ['nombre','genero','artista','album']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ['nombre','correo']

class PlaylistSerializer(serializers.ModelSerializer):
    user_nombre = serializers.CharField(source='user.nombre')
    class Meta:
        model = playlist
        fields = ['nombre','user_nombre']

class CancionDePlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = canciondeplaylist
        fields = ['cancion','playlist']
