from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db import models
from .serializers import *

# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):

    queryset = vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    def get_queryset(self):
        
        auto = self.request.vehiculo
        return vehiculo.objects.filter(vehiculo = auto)
    

class TipoViewSet(viewsets.ModelViewSet):
    queryset = tipo.objects.all()
    serializer_class = TipoSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = tipo.objects.all()
        descrip = self.request.query_params.get('descripcion')
        return queryset

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = marca.objects.all()
    serializer_class = MarcaSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = marca.objects.all()
        descrip = self.request.query_params.get('descripcion')
        return queryset
