from rest_framework import serializers
from .models import Song, Singer, Albun, Playlist, User


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

class AlbunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albun
        fields = '__all__'

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'