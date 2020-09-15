from django.shortcuts import render

from rest_framework import viewsets
from .models import Song, Singer, Albun, Playlist, User
from .serializers import SongSerializer, SingerSerializer, AlbunSerializer, PlaylistSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SongViewSet(viewsets.ModelViewSet): 
    queryset = Song.objects.all()
    serializer_class = SongSerializer 
    #permission_classes = (IsAuthenticated,) 
    


    
    musicname = models.CharField(max_length=50)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)
    idSinger = models.ForeignKey(Singer, on_delete = models.CASCADE)

    def __str__(self):

        return f"{self.musicname}, {self.genero}, {self.anio}"