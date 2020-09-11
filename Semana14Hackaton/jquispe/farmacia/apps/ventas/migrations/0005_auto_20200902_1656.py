# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20151127_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle_venta',
            name='medicamento',
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='Medicamentos',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]
