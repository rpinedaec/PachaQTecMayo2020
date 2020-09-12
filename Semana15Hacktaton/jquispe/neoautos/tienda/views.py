from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import generics
from tienda.serializers import VehiculoSerializer, TipoVehiculoSerializer, MarcaVehiculoSerializer

Create your views here.

class VehiculoList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehiculo.objects.all().order_by('-date_joined')
    serializer_class = VehiculoSerializer

class VehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objetos.all()
    serializer_class = VehiculoSerializer

    
    # def get_queryset(self):
    #     queryset = User.objects.all().order_by('-date_joined')
    #     username = self.request.query_params.get('username',None)
    #     if username is not None:
    #         queryset = queryset.filter(username= username)
    #     return queryset
    
class TipoVehiculoList(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TipoVehiculo.objects.all()
    serializer_class = TipoVehiculoSerializer

class TipoVehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoVehiculo.objetos.all()
    serializer_class = TipoVehiculoSerializer

class MarcaVehiculoList(generics.ListCreateApiView):
    queryset = MarcaVehiculo.objects.all()
    serializers_class = MarcaVehiculoSerializer

class MarcaVehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarcaVehiculo.objects.all()
    serializers_class = MarcaVehiculoSerializer