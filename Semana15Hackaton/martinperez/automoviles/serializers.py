
from rest_framework import serializers
from automoviles.models import automovil,tipo,marca


class tipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipo
        fields = ['descripcion', 'activo']

class marcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = marca
        fields = ['descripcion', 'activo']


class automovilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = automovil
        fields = ['descripcion','marca','tipo', 'activo']


