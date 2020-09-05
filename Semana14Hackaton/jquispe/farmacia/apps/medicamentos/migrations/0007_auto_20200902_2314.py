# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0006_auto_20151214_2306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Presentacion',
        ),
    ]
