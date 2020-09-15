from rest_framework import serializers

from hrkappmartin.models import Pelicula ,artista,cancion,album,playlist


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = artista
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = cancion
        fields = ('__all__')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = album
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = playlist
        fields = '__all__'

