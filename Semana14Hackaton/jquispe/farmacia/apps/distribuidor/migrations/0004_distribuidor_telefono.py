# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidor', '0003_remove_distribuidor_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidor',
            name='telefono',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
