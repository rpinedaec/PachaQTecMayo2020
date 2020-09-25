from django.shortcuts import render
from django.http import JsonResponse
from .models import tipoDocumento, Cliente, Producto, Tecnico, Factura, detalleFactura
from django.template import loader
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_date
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

# Create your views here.
def index(request):
    allClientes = Cliente.objects.all()
    allProductos = Producto.objects.all()
    allTecnicos = Tecnico.objects.all()
    context = {
        "clientes": allClientes,
        "productos": allProductos,
        "tecnicos": allTecnicos
    }
    return render(request, "productos/index.html", context)

def getClientes(request):
    queryset = Cliente.objects.all().values()
    return JsonResponse({"clientes": list(queryset)})

def getProductos(request):
    queryset = Producto.objects.all().values()
    return JsonResponse({"productos": list(queryset)})

@csrf_exempt
def setPedido(request):
    if request.method == 'POST':
        try:
            jsonData = json.loads(request.body)
            miCliente = Cliente.objects.get(id=int(jsonData["cab"]["cliente"]))
            mitransportista = Tecnico.objects.get(
                id=int(jsonData["cab"]["transportista"]))
            mipedido = Factura(
                tecnico=mitransportista,
                cliente=miCliente,
                fecha=parse_date(jsonData["cab"]["fecha"]),
                subtotal=float(jsonData["cab"]["subtotal"]),
                igv=float(jsonData["cab"]["igv"]),
                total=float(jsonData["cab"]["total"]))
            mipedido.save()
            idPedido = mipedido.id
            detalle = jsonData["det"]
            for objDetalle in detalle:
                miproducto = Producto.objects.get(id=int(objDetalle["id"]))
                cantidad = int(objDetalle["cant"])
                midetalle = detalleFactura(producto=miproducto,
                                          factura=mipedido,
                                          cantidad=cantidad)
                midetalle.save()

            return JsonResponse({"data": idPedido, "error":False})
        except Exception as e:
            return JsonResponse({"error": e})