# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('fecha_inicio', models.DateField()),
                ('concluido', models.BooleanField(default=False, verbose_name=b'Concluido?')),
                ('scrum_master', models.OneToOneField(null=True, blank=True, to='usuarios.Usuario')),
            ],
        ),
    ]
