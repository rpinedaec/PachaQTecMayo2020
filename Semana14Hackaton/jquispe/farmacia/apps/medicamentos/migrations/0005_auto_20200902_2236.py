# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0004_auto_20151214_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='igv',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
    ]
