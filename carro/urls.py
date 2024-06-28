from django.urls import path
from . import views

urlpatterns = [
    path('', views.carro_detalle, name="carro_detalle"),
    path('agregar/', views.carro_agregar, name="carro_agregar"),
    path('eliminar/', views.carro_eliminar, name="carro_eliminar"),
    path('actualizar/', views.carro_actualizar, name="carro_actualizar"),
    path('pdf/', views.generar_pdf, name='generar_pdf'),
]
