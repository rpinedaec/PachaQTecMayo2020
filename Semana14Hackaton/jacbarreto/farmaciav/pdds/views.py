from django.shortcuts import render
from .models import tipoCliente, tipoDocumento, tipoProducto, producto, cliente, pedido, detallePedido, vendedor
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_date
from django.views.decorators.http import require_http_methods
from .forms import tipoClienteForm
import logging#

def index(request):
    allClientes = cliente.objects.all()
    allProductos = producto.objects.all()
    #allTransportistas = transportista.objects.all()
    context = {
        "clientes": allClientes,
        "productos": allProductos,
        #"trasportistas": allTransportistas
    }
    return render(request, "pdds/index.html", context)


def getClientes(request):
    #queryset = cliente.objects.all().values()
    queryset = cliente.objects.all().filter(isActivo='AC').values()
    return JsonResponse({"clientes": list(queryset)})


def getProductos(request):
    queryset = producto.objects.all().values()
    return JsonResponse({"productos": list(queryset)})


def getVendedor(request):
    queryset = vendedor.objects.all().values()
    return JsonResponse({"vendedor": list(queryset)})

@csrf_exempt
def setPedido(request):
    logging.debug('setPedido WS')
    if request.method == 'POST':
        try:
            jsonData = json.loads(request.body)

            objCliente = cliente.objects.get(id=int(jsonData["cab"]["idCliente"]))
            objVendedor = vendedor.objects.get(id=int(jsonData["cab"]["idVendedor"]))
            fecha = parse_date(jsonData["cab"]["fecha"])
            subtotal = float(jsonData["cab"]["subtotal"])
            igv = float(jsonData["cab"]["igv"])
            total = float(jsonData["cab"]["total"])
            puntos = int(jsonData["cab"]["puntos"])
            mipedido = pedido(
                cliente = objCliente,
                vendedor = objVendedor,
                fecha = fecha,
                subtotal = subtotal,
                igv = igv,
                total = total)

            mipedido.save()
            idPedido = mipedido.id
            # miCliente = cliente.objects.get(id=int(jsonData["cab"]["cliente"]))
            # mivendedor = vendedor.objects.get(id=int(jsonData["cab"]["vendedor"]))   
            # #mitransportista = transportista.objects.get(
            #    # id=int(jsonData["cab"]["transportista"]))
            # mipedido = pedido(
            #     #transportista=mitransportista,
            #     cliente=miCliente,
            #     vendedor=mivendedor,
            #     fecha=parse_date(jsonData["cab"]["fecha"]),
            #     subtotal=float(jsonData["cab"]["subtotal"]), 
            #     igv=float(jsonData["cab"]["igv"]),
            #     total=float(jsonData["cab"]["total"]))        
            # mipedido.save()
            # idPedido = mipedido.id
            # detalle = jsonData["det"]
            # for objDetalle in detalle:
            #     miproducto = producto.objects.get(id=int(objDetalle["id"]))
            #     cantidad = int(objDetalle["cant"])
            #     midetalle = detallePedido(pedido=mipedido,
            #                               producto=miproducto,
            #                               cantidad=cantidad)
            #     midetalle.save()

            detalle = jsonData["det"]
            for objDetalle in detalle:
                miproducto = producto.objects.get(id=int(objDetalle["id"]))
                cantidad = int(objDetalle["cant"])
                precio = float(objDetalle["price"])
                midetalle = detallePedido(pedido=mipedido,
                                          producto=miproducto,
                                          cantidad=cantidad,
                                          precio=precio)
                midetalle.save()

            objCliente.puntos = objCliente.puntos + puntos
            objCliente.save()

            return JsonResponse({"data":idPedido, "error":False})
        except Exception as e:
            return JsonResponse({"data": e, "error": True})
            #return JsonResponse({"error": e})
        
        #return render(request, "template.html", c)
        #return JsonResponse('Hello world')

@require_http_methods(["GET", "POST"])
def setTipoCliente(request):
    if request.method == 'POST':
        tipo_ClienteForm = tipoClienteForm(request.POST)
        if tipo_ClienteForm.isValid():
            tipo_ClienteForm.save()
            return redirect("index")
        
    else:
        tipo_ClienteForm = tipoClienteForm()

    return render(request,"pdds/tipoCliente.html",{"tipoClienteForm": tipo_ClienteForm} )

            