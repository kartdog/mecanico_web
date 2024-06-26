from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name = 'index'),
    path('nosotros/', views.nosotros, name = 'nosotros'),
    # Productos
    path('producto/<int:pk>', views.producto, name = 'producto'),
    # Login
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    # Registro
    path('register/', views.register_user, name = 'register'),

]
