# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0006_tarea_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='concluido',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='en_desarrollo',
        ),
        migrations.AddField(
            model_name='tarea',
            name='estado',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'Pendiente', b'Pendiente'), (b'Desarrollo', b'Desarrollo'), (b'Concluido', b'Concluido')]),
        ),
    ]
