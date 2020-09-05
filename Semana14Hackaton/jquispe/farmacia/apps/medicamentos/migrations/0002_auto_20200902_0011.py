# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='fecha_expiracion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medicamentos',
            name='fecha_produccion',
            field=models.DateField(),
        ),
    ]
