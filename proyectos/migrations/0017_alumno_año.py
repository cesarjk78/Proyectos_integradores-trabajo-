# Generated by Django 5.1.2 on 2024-11-01 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0016_proyectointegrador_url_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='año',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectos.año'),
        ),
    ]
