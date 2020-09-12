# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20151127_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_venta',
            old_name='list',
            new_name='list_id',
        ),
    ]
