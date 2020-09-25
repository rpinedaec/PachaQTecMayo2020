from rest_framework import viewsets
from hrkapp.serializers import PeliculaSerializer
from hrkapp.models import Pelicula
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    #permission_classes = [IsAuthenticated,]
    #filter_backends = [DjangoFilterBackend]
   # filter_backends = [filters.SearchFilter]
    #search_fields = ['username', 'email']
   # search_fields=['code','name']