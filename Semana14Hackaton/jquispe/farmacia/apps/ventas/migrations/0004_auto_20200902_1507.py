# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20151127_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='list_id',
            field=models.ForeignKey(to='ventas.Cabecera_Venta'),
        ),
    ]
