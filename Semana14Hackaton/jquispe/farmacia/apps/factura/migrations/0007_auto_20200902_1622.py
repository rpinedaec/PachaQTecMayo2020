# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0006_auto_20151220_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(related_name=b'cabecera', db_column=b'factura_id', to='factura.Factura'),
        ),
    ]
