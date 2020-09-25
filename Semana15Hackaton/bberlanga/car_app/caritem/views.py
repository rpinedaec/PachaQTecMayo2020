from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CarItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CarItem as CarItemModel
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CarItem(APIView):
    authenthication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        caritems = CarItemModel.objects.all()
        serializer = CarItemSerializer(caritems, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CarItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

class CarItemDetails(APIView):
     
    def get_object(self, id):
        try:
            return CarItemModel.objects.get(id=id)
        except CarItemModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):
        caritem = self.get_object(id)
        serializer = CarItemSerializer(caritem)
        return Response(serializer.data)
 
 
 
    def put(self, request,id):
        caritem = self.get_object(id)
        serializer = CarItemSerializer(caritem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        caritem = self.get_object(id)
        caritem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)