# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20151111_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
