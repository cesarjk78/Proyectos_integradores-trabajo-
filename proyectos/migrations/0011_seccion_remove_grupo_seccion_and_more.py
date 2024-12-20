# Generated by Django 5.1.2 on 2024-10-31 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_alter_alumnoproyecto_alumno_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='seccion',
        ),
        migrations.AlterField(
            model_name='alumnoproyecto',
            name='alumno_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historialproyecto',
            name='fecha_actualizacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
