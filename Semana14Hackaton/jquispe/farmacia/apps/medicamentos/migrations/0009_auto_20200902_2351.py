# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0008_auto_20151214_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='igv',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=3),
        ),
    ]
