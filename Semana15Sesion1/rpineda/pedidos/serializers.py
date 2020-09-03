from rest_framework import serializers
from .models import tipoCliente

class TipoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipoCliente
        fields = ['descripcion', 'isActivo']
