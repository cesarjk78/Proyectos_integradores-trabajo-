from django.contrib import admin
from .models import CategoriaProyecto, ProyectoIntegrador, Documento, AlumnoProyecto, Comentario, HistorialProyecto


class ProyectoIntegradorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_presentacion', 'profesor')
    search_fields = ('titulo', 'descripcion')

class CategoriaProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


admin.site.register(CategoriaProyecto, CategoriaProyectoAdmin)
admin.site.register(ProyectoIntegrador, ProyectoIntegradorAdmin)
admin.site.register(Documento)
admin.site.register(AlumnoProyecto)
admin.site.register(Comentario)
admin.site.register(HistorialProyecto)
