from django.shortcuts import render
from factura.models import Producto


# Create your views here.

def lista(request):
    allProductos = Producto.objects.all()
    context = {
        "productos": allProductos,
    }
    return render(request, "productos/lista.html", context)