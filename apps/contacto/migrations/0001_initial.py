# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacto_name', models.CharField(max_length=45)),
                ('contacto_nacimiento', models.DateField()),
                ('contacto_sexo', models.CharField(max_length=50, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])),
                ('contacto_estado_civil', models.CharField(max_length=50, verbose_name=b'Estado Civil', choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viudo', 'Viudo')])),
                ('contacto_email', models.CharField(max_length=50)),
                ('contacto_favorito', models.BooleanField(verbose_name=b'Favorito')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuenta_name', models.CharField(max_length=50)),
                ('cuenta_data_vencimiento', models.DateField()),
                ('pago', models.BooleanField(verbose_name=b'Pago')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarea_nombre', models.CharField(max_length=120)),
                ('tarea_data_inicio', models.DateField(auto_now_add=True)),
                ('concluido', models.BooleanField(default=False, verbose_name=b'Concluido')),
            ],
        ),
    ]
