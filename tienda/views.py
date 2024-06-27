from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

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

# Registro
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Logea
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Te has registrado exitosamente!"))
            return redirect('index')
        else:
            messages.success(request, ("Ha ocurrido un error, intenta nuevamente."))
            return redirect('register')

    return render(request, 'register.html', {'form': form})

# Usuario
def actualizar_usuario(request):
    if request.user.is_authenticated:
        usuario_actual = User.objects.get(id=request.user.id)
        form_usuario = UpdateUserForm(request.POST or None, instance = usuario_actual)

        if form_usuario.is_valid():
            form_usuario.save()

            login(request, usuario_actual)
            messages.success(request, "Usuario ha sido actualizado!")
            return redirect('index')
        return render(request, 'actualizar_usuario.html', {'form_usuario': form_usuario})
    else:
        messages.success(request, "Debes iniciar sesión para acceder a esa página.")
        return redirect('index')

    return render(request, 'actualizar_usuario.html', {})

# Empleado
def empleados(request):
    empleados = Empleado.objects.all() # SELECT * FROM empleado

    aux = {
        'lista' : empleados
    }

    return render(request, 'tienda/empleados/index.html', aux)

# @permission_required('tienda.add_empleado')
def empleadosadd(request):
    aux = {
            'form' : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Empleado almacenado correctamente!'
            return redirect('empleados')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo almacenar :('

    return render(request, 'tienda/empleados/crud/add.html', aux)

def empleadosupdate(request, id):
    empleado = Empleado.objects.get(id=id)
    aux = {
            'form' : EmpleadoForm(instance = empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data = request.POST, instance = empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Empleado modificado correctamente!'
            return redirect('empleados')
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo modificar :('

    return render(request, 'tienda/empleados/crud/update.html', aux)

@permission_required('tienda.delete_empleado')
def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")

# Producto
def producto(request, pk):
    producto = Producto.objects.get(id=pk)
    return render(request, 'producto.html', {'producto': producto})

# Categoria
def categoria(request, foo):
    foo = foo.replace('-', ' ')
    try:
        categoria = Categoria.objects.get(nombre=foo)
        productos = Producto.objects.filter(categoria=categoria)
        return render(request, 'categoria.html', {'productos': productos, 'categoria': categoria})
    except:
        messages.success(request, ("La categoria no existe."))
        return redirect('index')