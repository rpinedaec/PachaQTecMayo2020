from django.contrib.auth.models import User, Group
from lista.models import Album, Artista, Cancion, CancionPlaylist, Playlist, Usuario
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        
class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'
        
class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'
        
class CancionPlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CancionPlaylist
        fields = '__all__'
        
class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'