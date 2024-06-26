from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .carro import Carro
from tienda.models import Producto

def carro_detalle(request):
    return render(request, "carro_detalle.html", {})

def carro_agregar(request):
    carro = Carro(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto_id'))
        producto = get_object_or_404(Producto, id=producto_id)
        carro.agregar(producto=producto)

        response = JsonResponse({'Producto: ': producto.nombre})
        return response

def carro_eliminar(request):
    pass

def carro_actualizar(request):
    pass
