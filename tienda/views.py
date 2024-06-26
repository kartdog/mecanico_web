from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Inicio
def index(request):
    productos = Producto.objects.all()

    return render(request, 'index.html', {'productos': productos})

def nosotros(request):
    return render(request, 'nosotros.html', {})

# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Has iniciado sesión."))
            return redirect('index')
        else:
            messages.success(request, ("Ha ocurrido un error, intenta nuevamente."))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Has cerrado la sesión."))
    return redirect('index')