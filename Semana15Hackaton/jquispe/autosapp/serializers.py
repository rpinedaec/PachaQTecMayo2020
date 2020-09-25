from rest_framework import serializers
from .models import *

class VehiculoSerializer(serializers.Serializer):
    
    class Meta:
    
        model = vehiculo
        fields = '__all__'

class TipoSerializer(serializers.Serializer):

    class Meta:

        model = tipo
        fields = '__all__'

class MarcaSerializer(serializers.Serializer):

    class Meta:

        model = marca
        fields = '__all__'
