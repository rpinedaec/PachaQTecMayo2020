from rest_framework import viewsets
#from rest_framework import permissions
from pedidos.serializers import CategoriaSerializer, MarcaSerializer, ModeloSerializer, TipoAutoSerializer, AutoSerializer
from pedidos.models import categoria, marca, modelo, tipoAuto, auto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        queryset = categoria.objects.all()
        desc = self.request.query_params.get('desc',None)
        if desc is not None:
            queryset = queryset.filter(descripcion=desc)
        return queryset

    def post_queryset(self, request):
        categoria.save()
        #return queryset
        return Response(status=201)
    
class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        queryset = marca.objects.all()
        desc = self.request.query_params.get('desc',None)
        #queryset = marca.objects.filter(descripcion=desc)
        if desc is not None:
           queryset = queryset.filter(descripcion=desc)
        return queryset

    def post_queryset(self, request):
        marca.save()
        #return queryset
        return Response(status=201)

    
class ModeloViewSet(viewsets.ModelViewSet):
    serializer_class = ModeloSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        queryset = modelo.objects.all()
        desc = self.request.query_params.get('desc',None)
        if desc is not None:
            queryset = queryset.filter(descripcion=desc)
        return queryset

    def post_queryset(self, request):
        modelo.save()
        #return queryset
        return Response(status=201)

class TipoAutoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoAutoSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        queryset = tipoAuto.objects.all()
        desc = self.request.query_params.get('desc',None)
        if desc is not None:
            queryset = queryset.filter(descripcion=desc)
        return queryset

    def post_queryset(self, request):
        tipoAuto.save()
        #return queryset
        return Response(status=201)

class AutoViewSet(viewsets.ModelViewSet):
    serializer_class = AutoSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        queryset = auto.objects.all()
        # placa = self.request.query_params.get('nplaca','color', 'anio', 'km', 'combustible', 'motor',
        #  'nropuertas', 'tapiceria', 'costo', 'isActivo', None)
        placa = self.request.query_params.get('placa', None)
        if placa is not None:
            queryset = queryset.filter(nplaca=placa)
        return queryset
    
    def post_queryset(self, request):
        auto.save()
        #return queryset
        return Response(status=201)
    
    
   