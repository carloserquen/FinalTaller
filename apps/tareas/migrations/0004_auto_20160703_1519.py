# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_tarea_en_desarrollo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]
