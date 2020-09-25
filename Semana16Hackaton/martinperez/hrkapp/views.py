from rest_framework import viewsets
from hrkapp.serializers import PeliculaSerializer
from hrkapp.models import Pelicula

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer