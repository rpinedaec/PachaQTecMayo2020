# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20151106_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera',
            name='codigo',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
