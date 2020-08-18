from django.shortcuts import render
from .models import tipoCliente, tipoDocumento, tipoProducto, producto, cliente, transportista
from django.http import JsonResponse

def index(request):
    allClientes = cliente.objects.all()
    allProductos = producto.objects.all()
    allTransportistas = transportista.objects.all()
    context = {
        "clientes": allClientes,
        "productos": allProductos,
        "trasportistas": allTransportistas
    }
    return render(request, "pdds/index.html", context)


def getClientes(request):
    #data =  cliente.objects.all()
    queryset = cliente.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"clientes": list(queryset)})

def getTransportistas(request):
    #data =  cliente.objects.all()
    queryset = transportista.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"transportistas": list(queryset)})

def getProductos(request):
    #data =  cliente.objects.all()
    queryset = producto.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"productos": list(queryset)})