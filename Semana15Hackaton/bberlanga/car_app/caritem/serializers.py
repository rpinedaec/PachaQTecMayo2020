from rest_framework import serializers
from .models import CarItem

class CarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = ['id_brand','id_type','id_model','price','year']
