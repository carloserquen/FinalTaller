# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='contacto_estado_civil',
            field=models.CharField(max_length=50, choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viudo', 'Viudo')], verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='contacto_favorito',
            field=models.BooleanField(verbose_name='Favorito'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='pago',
            field=models.BooleanField(verbose_name='Pago'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='concluido',
            field=models.BooleanField(default=False, verbose_name='Concluido'),
        ),
    ]
