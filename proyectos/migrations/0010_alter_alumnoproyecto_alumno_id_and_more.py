# Generated by Django 5.1.2 on 2024-10-31 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0009_remove_proyectointegrador_documento_pdf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnoproyecto',
            name='alumno_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='historialproyecto',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]