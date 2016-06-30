# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_auto_20160618_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='proyecto_data_inicio',
            new_name='fecha_inicio',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='proyecto_nombre',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='concluido',
            field=models.BooleanField(default=False, verbose_name=b'Concluido?'),
        ),
    ]
