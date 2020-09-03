# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_factura_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='CategoriaProducto',
        ),
        migrations.RemoveField(
            model_name='detallefactura',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
