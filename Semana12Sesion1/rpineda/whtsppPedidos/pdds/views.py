from django.shortcuts import render
from .models import tipoClientes, tipoDocumentos, tipoProductos, productos, clientes, transportistas

def index(request):
    allClientes = clientes.objects.all()
    allProductos = productos.objects.all()
    allTransportistas = transportistas.objects.all()
    context = {
        "clientes":allClientes,
        "productos":allProductos,
        "trasportistas":allTransportistas
    }
    return render(request,"pdds/index.html", context)
