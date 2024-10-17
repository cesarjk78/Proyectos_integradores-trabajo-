from django.contrib import admin
from .models import Rol, Usuario, CategoriaProyecto, ProyectoIntegrador, Documento, AlumnoProyecto, Comentario, HistorialProyecto

# Registro de los modelos sin duplicados

class ProyectoIntegradorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_presentacion', 'anio', 'profesor')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('anio', 'categoria')

class CategoriaProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol')

# Registra los modelos aquí
admin.site.register(Rol)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(CategoriaProyecto, CategoriaProyectoAdmin)
admin.site.register(ProyectoIntegrador, ProyectoIntegradorAdmin)
admin.site.register(Documento)
admin.site.register(AlumnoProyecto)
admin.site.register(Comentario)
admin.site.register(HistorialProyecto)
