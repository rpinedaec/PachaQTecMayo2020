from django.http import HttpResponse
from django.db import models
from .models import Producto


def index(request):
    miProducto = Producto.objects.filter(id=1)
    miProducto[0].nombre = "Pera"
    miProducto[0].save()
    nuevoProducto = miProducto[0]
    nuevoProducto.nombre = "Pera"
    nuevoProducto.save()
     
    return HttpResponse(f"Hola a mi primera vista de: \n {miProducto[0].nombre}")