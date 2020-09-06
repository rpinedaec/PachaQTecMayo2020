from django.contrib.auth.models import User, Group
from coches.models import Modelo, Marca, Auto
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modelo
        fields = ['url', 'descripcion']

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['url', 'descripcion', 'modelo']

class AutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ['url', 'descripcion', 'marca', 'color']