from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrar/', views.crear_usuario, name='registrar'),
    path('proyectos/', views.listar_proyectos, name='proyectos'),
    path('detalle/<int:proyecto_id>/', views.detalles_proyecto, name='detalles_proyecto'), 
]
