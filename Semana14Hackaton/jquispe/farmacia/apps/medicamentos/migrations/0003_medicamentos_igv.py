# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_auto_20151014_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamentos',
            name='igv',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
