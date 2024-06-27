from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *

# Configuracion urls para API
router = routers.DefaultRouter()
router.register('empleados', EmpleadoViewSet)
router.register('servicios', ServicioViewSet)

urlpatterns = [
    # Index
    path('', views.index, name = 'index'),
    path('nosotros/', views.nosotros, name = 'nosotros'),
    # Productos
    path('productos/', views.productos, name="productos"),
    path('productos/<int:pk>', views.producto_id, name = 'producto_id'),
    path('productos/add/', views.productosadd, name="productosadd"),
    path('productos/crud/update/<id>/', views.productosupdate, name="productosupdate"),
    path('productos/crud/delete/<id>/', views.productosdelete, name="productosdelete"),
    # Servicios
    path('servicios/', views.servicios, name="servicios"),
    path('servicios/add/', views.serviciosadd, name="serviciosadd"),
    path('servicios/crud/update/<id>/', views.serviciosupdate, name="serviciosupdate"),
    path('servicios/crud/delete/<id>/', views.serviciosdelete, name="serviciosdelete"),
    # Categorias
    path('categoria/<str:foo>', views.categoria, name = 'categoria'),
    # Login
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    # Registro
    path('register/', views.register_user, name = 'register'),
    # Usuario
    path('actualizar_usuario/', views.actualizar_usuario, name = 'actualizar_usuario'),
    # Empleados
    path('empleados/', views.empleados, name="empleados"),
    path('empleados/add/', views.empleadosadd, name="empleadosadd"),
    path('empleados/crud/update/<int:id>/', views.empleadosupdate, name="empleadosupdate"),
    path('empleados/crud/delete/<int:id>/', views.empleadosdelete, name="empleadosdelete"),
    # API
    path('api/', include(router.urls)),
    path('empleadosapi/', empleadosapi, name="empleadosapi"),
    path('serviciosapi/', serviciosapi, name="serviciosapi"),
]