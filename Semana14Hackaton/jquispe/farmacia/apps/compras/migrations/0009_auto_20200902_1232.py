# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_auto_20151220_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cabecera',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
