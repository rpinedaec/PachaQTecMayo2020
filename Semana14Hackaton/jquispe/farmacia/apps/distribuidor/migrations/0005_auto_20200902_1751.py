# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidor', '0004_distribuidor_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribuidor',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='distribuidor',
            name='ruc',
            field=models.IntegerField(unique=True),
        ),
    ]
