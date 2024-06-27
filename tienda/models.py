from django.db import models
import datetime

# Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='uploads/empleado/', null=True, blank=True)

    def __str__(self):
        return self.nombre

# Cliente
class Cliente(models.Model):
    p_nombre = models.CharField(max_length=50)
    s_nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.p_nombre} {self.s_nombre}'
    
    class Meta:
        verbose_name_plural = 'Clientes'

# Categoria de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Categorias'

# Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    descripcion = models.CharField(max_length=250, default='', blank=True, null= True)
    imagen = models.ImageField(upload_to='uploads/product/')

    # En Oferta
    is_oferta = models.BooleanField(default=False)
    oferta_precio = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.nombre    
    
    class Meta:
        verbose_name_plural = 'Productos'

# Servicio
class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=200)
    descripcion_servicio = models.TextField(max_length=550)
    imagen_servicio = models.ImageField(upload_to='uploads/servicio/', null=True, blank=True)
    def __str__(self):
        return self.nombre_servicio

# Orden
class Orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    direccion = models.CharField(max_length=100, default='', blank=True)
    telefono = models.CharField(max_length=50, default='', blank=True)
    fecha = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.producto
    
    class Meta:
        verbose_name_plural = 'Ordenes'