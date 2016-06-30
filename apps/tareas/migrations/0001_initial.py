# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20160629_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('concluido', models.BooleanField(default=False, verbose_name=b'Concluido?')),
                ('proyecto', models.ForeignKey(to='proyectos.Proyecto')),
            ],
        ),
    ]
