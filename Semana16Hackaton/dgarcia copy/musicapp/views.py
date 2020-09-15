from rest_framework import viewsets
from musicapp.serializers import ArtistaSerializer
from musicapp.models import Artista
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    #permission_classes = [IsAuthenticated,]
    #filter_backends = [DjangoFilterBackend]
   # filter_backends = [filters.SearchFilter]
    #search_fields = ['username', 'email']
   # search_fields=['code','name']