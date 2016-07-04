# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0004_auto_20160703_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='fecha_inicio',
            new_name='fecha_terminar',
        ),
    ]
