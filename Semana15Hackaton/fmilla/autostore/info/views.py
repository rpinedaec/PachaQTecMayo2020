from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework import permissions
from info.serializers import ModeloSerializer, MarcaSerializer, TipoSerializer, AutoSerializer
from info.models import marca, modelo, tipo, auto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = marca.objects.all()
        desc = self.request.query_params.get('desc',None)
        if desc is not None:
            queryset = queryset.filter(nombre=desc)
        return queryset

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = modelo.objects.all()
    serializer_class = ModeloSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre']

class TipoViewSet(viewsets.ModelViewSet):
    queryset = tipo.objects.all()
    serializer_class = TipoSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['descripcion']

class AutoViewSet(viewsets.ModelViewSet):
    queryset = auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    raw_id_fields = ('marca','modelo','tipo')
    search_fields=['codigo','marca__nombre','modelo__nombre','tipo__descripcion']

