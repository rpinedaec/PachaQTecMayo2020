from rest_framework import serializers
from tienda.models import 


class VehiculoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class TipoVehiculoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'

class MarcaVehiculoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MarcaVehiculo
        fields = '__all__'