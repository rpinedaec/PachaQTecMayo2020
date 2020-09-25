# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_medicamentos_igv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='igv',
            field=models.DecimalField(max_digits=6, decimal_places=6),
        ),
    ]
