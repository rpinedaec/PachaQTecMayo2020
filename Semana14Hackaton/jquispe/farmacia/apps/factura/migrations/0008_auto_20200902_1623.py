# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0007_auto_20151228_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(related_name=b'factura', db_column=b'factura_id', to='factura.Factura'),
        ),
    ]
