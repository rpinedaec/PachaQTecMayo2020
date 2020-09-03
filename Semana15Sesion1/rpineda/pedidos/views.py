from rest_framework import viewsets
from rest_framework import permissions
from pedidos.serializers import TipoClienteSerializer
from pedidos.models import tipoCliente

class TipoClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = tipoCliente.objects.all()
    serializer_class = TipoClienteSerializer
    permission_classes = [permissions.IsAuthenticated]