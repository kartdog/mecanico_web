from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    productos = Producto.objects.all()

    return render(request, 'index.html', {'productos': productos})

def nosotros(request):

    return render(request, 'nosotros.html', {})