# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='tarea_descripcion',
            field=models.TextField(default='holi'),
            preserve_default=False,
        ),
    ]
