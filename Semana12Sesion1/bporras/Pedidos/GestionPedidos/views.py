from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import producto, tipoProducto
from GestionPedidos.forms import FormularioTipoProducto

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):
    if  request.GET["prd"] :
        # mensaje = f'Articulo buscado: {request.GET["prd"]}'
        prd = request.GET["prd"]
        if len(prd) > 20 :
            mensaje = 'Texto de busqueda demasiado largo'
        else:
            productos = producto.objects.filter(nombre__icontains=prd)
            return render(request, "resultados_busqueda.html", {"productos": productos, "query": prd})
    else:
        mensaje = 'No haz intruducido nada'
    return HttpResponse(mensaje)

def tipo_producto(request):

    if request.method == "POST":
        miFormulario = FormularioTipoProducto(reques.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.changed_data
            descripcion = infForm['descripcion']
            estado = infForm['estado']
            