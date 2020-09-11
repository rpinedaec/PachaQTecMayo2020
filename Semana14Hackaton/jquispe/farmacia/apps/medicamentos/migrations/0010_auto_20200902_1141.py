# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0009_auto_20151214_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='lote',
            field=models.CharField(default=0, unique=True, max_length=10),
        ),
    ]
