# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('tareas', '0005_auto_20160703_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='owner',
            field=models.ForeignKey(to='usuarios.Usuario', null=True),
        ),
    ]
