# Generated by Django 5.1.2 on 2024-10-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0013_remove_proyectointegrador_fecha_presentacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectointegrador',
            name='semestre',
            field=models.IntegerField(choices=[(1, '1'), (2, '2')], default=1),
        ),
    ]
