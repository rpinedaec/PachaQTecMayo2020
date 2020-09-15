from rest_framework import serializers

from hrkapp.models import Pelicula


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

