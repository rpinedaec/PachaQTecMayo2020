# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20151106_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='list',
            field=models.ForeignKey(related_name=b'cabecera', to='compras.Cabecera'),
        ),
    ]
