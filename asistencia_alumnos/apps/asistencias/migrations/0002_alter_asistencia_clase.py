# Generated by Django 5.0.6 on 2024-05-29 03:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0001_initial'),
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias_relacion', to='clases.clase'),
        ),
    ]
