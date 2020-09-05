# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20151007_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecompra',
            old_name='compra',
            new_name='list',
        ),
    ]
