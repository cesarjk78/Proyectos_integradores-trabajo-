from django.urls import path
from . import views  # Importar las vistas desde el archivo views.py

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista principal de la app
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
]