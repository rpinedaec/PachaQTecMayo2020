from rest_framework import viewsets
#from rest_framework import permissions
from automoviles.models import automovil,tipo,marca
from automoviles.serializers import tipoSerializer, marcaSerializer,automovilSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TipoViewSet(viewsets.ModelViewSet): 
    serializer_class = tipoSerializer 
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = tipo.objects.all()
        descrip = self.request.query_params.get('descripcion',None)
        if descrip is not None:
            queryset = queryset.filter(descripcion=descrip)
        return queryset


class MarcaViewSet(viewsets.ModelViewSet): 
    serializer_class = marcaSerializer 
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = marca.objects.all()
        descrip = self.request.query_params.get('descripcion',None)
        if descrip is not None:
            queryset = queryset.filter(descripcion=descrip)
        return queryset

class AutomovilViewSet(viewsets.ModelViewSet): 
    serializer_class = automovilSerializer 
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = automovil.objects.all()
        descrip = self.request.query_params.get('descripcion',None)
        if descrip is not None:
            queryset = queryset.filter(descripcion=descrip)
        return queryset


class AutomoviPorTipoViewSet(viewsets.ModelViewSet): 
    serializer_class = automovilSerializer 
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = automovil.objects.all()
        descrip = self.request.query_params.get('tipo',None)
        if descrip is not None:
            queryset = queryset.filter(descripcion=descrip)
        return queryset


class AutomoviPorMarcaViewSet(viewsets.ModelViewSet): 
    serializer_class = automovilSerializer 
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = automovil.objects.all()
        descrip = self.request.query_params.get('marca',None)
        if descrip is not None:
            queryset = queryset.filter(descripcion=descrip)
        return queryset
