from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .carro import *
from tienda.models import Producto

def carro_detalle(request):

    carro = Carro(request)
    carro_productos = carro.get_producto()

    cantidades = carro.get_cantidades

    return render(request, "carro_detalle.html", {"carro_productos": carro_productos, "cantidades": cantidades})

def carro_agregar(request):
    carro = Carro(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto_id'))
        producto_qty = int(request.POST.get('producto_qty'))

        producto = get_object_or_404(Producto, id=producto_id)
        carro.agregar(producto=producto, cantidad=producto_qty)

        carro_cantidad = carro.__len__()

        # response = JsonResponse({'Producto: ': producto.nombre})
        response = JsonResponse({'qty': carro_cantidad})
        return response

def carro_eliminar(request):
    pass

def carro_actualizar(request):
    carro = Carro(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto_id'))
        producto_qty = int(request.POST.get('producto_qty'))

        carro.actualizar(producto= producto_id, cantidad = producto_qty)

        response = JsonResponse({'qty': producto_qty})
        return response
