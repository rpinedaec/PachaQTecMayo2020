from django.shortcuts import render
from .models import tipoCliente, tipoDocumento, tipoProducto, producto, cliente, pedido, detallePedido
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_date
from django.views.decorators.http import require_http_methods
from administración.forms import tipoClienteForm

def index(request):
    allClientes = cliente.objects.all()
    allProductos = producto.objects.all()
    context = {
        "clientes": allClientes,
        "productos": allProductos,
    }
    return render(request, "admin/index.html", context)


def getClientes(request):
    queryset = cliente.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"clientes": list(queryset)})


def getProductos(request):
    queryset = producto.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"productos": list(queryset)})


@csrf_exempt
def estadoPedido(request, idPedido):
    if request.method == 'GET':
        values = pedido.objects.get(id=idPedido)
        serialized_obj = serializers.serialize('json', [values, ])
        return JsonResponse({"data": serialized_obj})
        # mipedido = pedido.objects.get(id=idPedido)
        # serialized_obj = serializers.serialize('json', [ mipedido, ])
        # return JsonResponse({"data":serialized_obj})
    elif request.method == 'POST':
        # request.raw_post_data w/ Django < 1.4
        json_data = json.loads(request.body)
        try:
            data = json_data['estado']
            miPedido = pedido.objects.get(id=idPedido)
            miPedido.estado = data
            miPedido.save()
        except KeyError:
            return JsonResponse({"error": "No esta bien el json"})
        return JsonResponse({"idPedido": idPedido, "Metodo": "POST", "data": data})


@csrf_exempt
def ubicacionPedido(request, idPedido):
    if request.method == 'GET':
        values = pedido.objects.get(id=idPedido)
        serialized_obj = serializers.serialize('json', [values, ])
        return JsonResponse({"data": serialized_obj})
    elif request.method == 'POST':
        # request.raw_post_data w/ Django < 1.4
        json_data = json.loads(request.body)
        try:
            data = json_data['ubicacion']
            miPedido = pedido.objects.get(id=idPedido)
            miPedido.ubicacion = data
            miPedido.save()
        except KeyError:
            return JsonResponse({"error": "No esta bien el json"})
        return JsonResponse({"idPedido": idPedido, "Metodo": "POST", "data": data})


@csrf_exempt
def setPedido(request):
    if request.method == 'POST':
        try:
            jsonData = json.loads(request.body)
            miCliente = cliente.objects.get(id=int(jsonData["cab"]["cliente"]))
            mipedido = pedido(
                cliente=miCliente,
                fecha=parse_date(jsonData["cab"]["fecha"]),
                subtotal=float(jsonData["cab"]["subtotal"]),
                igv=float(jsonData["cab"]["igv"]),
                total=float(jsonData["cab"]["total"]))
            mipedido.save()
            idPedido = mipedido.id
            detalle = jsonData["det"]
            for objDetalle in detalle:
                miproducto = producto.objects.get(id=int(objDetalle["id"]))
                cantidad = int(objDetalle["cant"])
                midetalle = detallePedido(producto=miproducto,
                                          pedido=mipedido,
                                          cantidad=cantidad)
                midetalle.save()

            return JsonResponse({"data": idPedido, "error":False})
        except Exception as e:
            return JsonResponse({"error": e})

@require_http_methods(["GET", "POST"])
def setTipoCliente(request):
    if request.method == 'POST':
        tipo_ClienteForm = tipoClienteForm(request.POST)
        if tipo_ClienteForm.isValid():
            tipo_ClienteForm.save()
            return redirect("index")
        
    else:
        tipo_ClienteForm = tipoClienteForm()

    return render(request,"admin/tipoCliente.html",{"tipoClienteForm": tipo_ClienteForm} )