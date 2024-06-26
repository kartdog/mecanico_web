from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
    path('carro/', include('carro.urls')),
    path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)