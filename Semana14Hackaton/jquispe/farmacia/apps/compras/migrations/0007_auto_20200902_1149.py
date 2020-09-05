# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_cabecera_trabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabecera',
            name='created',
            field=models.DateTimeField(default=datetime.date(2015, 11, 11), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cabecera',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2015, 11, 11), auto_now=True),
            preserve_default=False,
        ),
    ]
