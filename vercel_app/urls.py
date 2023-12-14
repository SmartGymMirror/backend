from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('example.urls')),
    path('auth/', include('djoser.urls')),  # URLs generales de autenticación
    path('auth/', include('djoser.urls.jwt')),  # URLs JWT
    path('', TemplateView.as_view(template_name='index.html')),  # Ruta específica para el TemplateView
]
