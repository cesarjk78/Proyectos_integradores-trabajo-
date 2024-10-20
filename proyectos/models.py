from django.db import models
from django.contrib.auth.models import User

class CategoriaProyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class ProyectoIntegrador(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_presentacion = models.DateField()
    profesor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Documento(models.Model):
    TIPO_DOCUMENTO = [
        ('documento', 'Documento'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
    ]
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_DOCUMENTO)
    url = models.URLField()
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class AlumnoProyecto(models.Model):
    alumno = models.CharField(max_length=255)
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE)
    fecha_descarga = models.DateTimeField()

    def __str__(self):
        return f"{self.alumno} - {self.proyecto}"

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.fecha_comentario}"

class HistorialProyecto(models.Model):
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField()

    def __str__(self):
        return f"Version {self.version} - {self.titulo}"
