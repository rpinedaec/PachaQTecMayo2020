from rest_framework import serializers
from .models import categoria, marca, modelo, tipoAuto, auto 
#tipoCliente, tipoProducto

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categoria
        fields = ['descripcion', 'isActivo']

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = marca
        fields = ['descripcion', 'isActivo']

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modelo
        fields = ['descripcion', 'isActivo']

class TipoAutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipoAuto
        fields = ['descripcion', 'isActivo']

class AutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auto
        fields = ['nplaca', 'color' , 'anio' , 'km' , 'combustible' , 'motor' ,
        'nropuertas' , 'tapiceria' , 'costo'  ,'isActivo','categoria_id','marca_id', 'modelo_id','tipoAuto_id']

# class TipoClienteSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = tipoCliente
#         fields = ['descripcion', 'isActivo']

# class TipoProductoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = tipoProducto
#         fields = ['descripcion', 'isActivo']
