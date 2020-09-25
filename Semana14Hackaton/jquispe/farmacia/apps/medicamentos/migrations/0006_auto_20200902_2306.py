# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0005_auto_20151214_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicamentos',
            old_name='codigo',
            new_name='lote',
        ),
    ]
