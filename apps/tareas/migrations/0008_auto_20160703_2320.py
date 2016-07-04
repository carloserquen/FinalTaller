# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0007_auto_20160703_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='owner',
            field=models.ForeignKey(blank=True, to='usuarios.Usuario', null=True),
        ),
    ]
