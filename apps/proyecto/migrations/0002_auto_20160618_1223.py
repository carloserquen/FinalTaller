# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('proyecto_nombre', models.CharField(max_length=120)),
                ('proyecto_data_inicio', models.DateField(auto_now_add=True)),
                ('concluido', models.BooleanField(default=False, verbose_name='Concluido')),
            ],
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
        migrations.DeleteModel(
            name='Tarea',
        ),
    ]
