from .models import modelo, marca, tipo, auto
from rest_framework import serializers

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = marca
        fields = ['nombre']

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modelo
        fields = ['nombre']

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipo
        fields = ['descripcion']

class AutoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source='marca.nombre')
    modelo_nombre = serializers.CharField(source='modelo.nombre')
    tipo_descripcion = serializers.CharField(source='tipo.descripcion')

    class Meta:
        model = auto
        fields = ['codigo','marca_nombre','modelo_nombre','tipo_descripcion']

