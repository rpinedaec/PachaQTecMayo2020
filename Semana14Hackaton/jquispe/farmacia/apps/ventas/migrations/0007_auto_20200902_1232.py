# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_auto_20151127_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera_venta',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cabecera_venta',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
