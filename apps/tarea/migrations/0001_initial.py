# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tarea_nombre', models.CharField(max_length=120)),
                ('tarea_data_inicio', models.DateField(auto_now_add=True)),
                ('concluido', models.BooleanField(default=False, verbose_name='Concluido')),
            ],
        ),
    ]
