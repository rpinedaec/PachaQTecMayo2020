from rest_framework import viewsets
from pedidos.serializers import TipoClienteSerializer, TipoProductoSerializer
from pedidos.models import tipoCliente, tipoProducto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TipoClienteViewSet(viewsets.ModelViewSet):
    serializer_class = TipoClienteSerializer
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        queryset = tipoCliente.objects.all()
        desc = self.request.query_params.get('desc',None)
        if desc is not None:
            queryset = queryset.filter(descripcion=desc)
        return queryset

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = tipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
    permission_classes = [IsAuthenticated,]
    #filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    #search_fields = ['username', 'email']
    search_fields=['descripcion','isActivo']