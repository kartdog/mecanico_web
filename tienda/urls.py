from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name = 'index'),
    path('nosotros/', views.nosotros, name = 'nosotros'),
    # Productos
    path('producto/<int:pk>', views.producto, name = 'producto'),
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
]