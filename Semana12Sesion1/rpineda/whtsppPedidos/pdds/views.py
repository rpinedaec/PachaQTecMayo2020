from django.shortcuts import render
from .models import tipoCliente, tipoDocumento, tipoProducto, producto, cliente, transportista, pedido, detallePedido
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json



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
    queryset = cliente.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"clientes": list(queryset)})


def getTransportistas(request):
    queryset = transportista.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"transportistas": list(queryset)})


def getProductos(request):
    queryset = producto.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"productos": list(queryset)})

@csrf_exempt
def estadoPedido(request,idPedido):
    if request.method == 'GET':
        values = pedido.objects.get(id=idPedido)
        serialized_obj = serializers.serialize('json', [ values, ])
        return JsonResponse({"data": serialized_obj})
        # mipedido = pedido.objects.get(id=idPedido)
        # serialized_obj = serializers.serialize('json', [ mipedido, ])
        # return JsonResponse({"data":serialized_obj})
    elif request.method == 'POST':
        json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
        try:
            data = json_data['estado']
            miPedido = pedido.objects.get(id=idPedido)
            miPedido.estado = data
            miPedido.save()
        except KeyError:
            return JsonResponse({"error":"No esta bien el json"})
        return JsonResponse({"idPedido":idPedido, "Metodo":"POST", "data":data})

@csrf_exempt
def ubicacionPedido(request,idPedido):
    if request.method == 'GET':
        values = pedido.objects.get(id=idPedido)
        serialized_obj = serializers.serialize('json', [ values, ])
        return JsonResponse({"data": serialized_obj})
    elif request.method == 'POST':
        json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
        try:
            data = json_data['ubicacion']
            miPedido = pedido.objects.get(id=idPedido)
            miPedido.ubicacion = data
            miPedido.save()
        except KeyError:
            return JsonResponse({"error":"No esta bien el json"})
        return JsonResponse({"idPedido":idPedido, "Metodo":"POST", "data":data})