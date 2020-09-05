from rest_framework import serializers
from .models import tipoCliente, tipoProducto

class TipoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipoCliente
        fields = ['descripcion', 'isActivo']

class TipoProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipoProducto
        fields = ['descripcion', 'isActivo']
