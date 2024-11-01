from django.contrib import admin
from .models import CategoriaProyecto, Año, ProyectoIntegrador, Seccion, Grupo, Alumno, AlumnoProyecto, Comentario, HistorialProyecto, Valoracion

@admin.register(CategoriaProyecto)
class CategoriaProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Año)
class AñoAdmin(admin.ModelAdmin):
    list_display = ('año', 'semestre')
    list_filter = ('año', 'semestre')

@admin.register(ProyectoIntegrador)
class ProyectoIntegradorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'año', 'categoria', 'url_github')
    list_filter = ('año', 'categoria')
    search_fields = ('titulo', 'descripcion')
    
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descripcion', 'año', 'categoria')
        }),
        ('Media', {
            'fields': ('imagen', 'documento', 'video', 'url_github'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion')
    list_filter = ('seccion',)
    search_fields = ('nombre',)

from django.contrib import admin
from .models import Alumno, Año

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'grupo', 'seccion', 'año')  # Añadido 'año'
    list_filter = ('grupo', 'seccion', 'año')  # Añadido 'año'
    search_fields = ('nombre', 'apellido')


@admin.register(AlumnoProyecto)
class AlumnoProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'grupo', 'seccion', 'año')
    list_filter = ('grupo', 'seccion', 'año')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'fecha_comentario', 'usuario', 'proyecto')
    list_filter = ('fecha_comentario', 'usuario', 'proyecto')
    search_fields = ('contenido',)

@admin.register(HistorialProyecto)
class HistorialProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'titulo', 'fecha_actualizacion', 'version')
    list_filter = ('fecha_actualizacion', 'version')
    search_fields = ('titulo',)

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'proyecto', 'estrellas')
    list_filter = ('estrellas',)
    search_fields = ('usuario__username', 'proyecto__titulo')
