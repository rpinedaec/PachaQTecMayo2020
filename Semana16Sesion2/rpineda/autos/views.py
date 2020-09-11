from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from autos.models import Car
from autos.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
