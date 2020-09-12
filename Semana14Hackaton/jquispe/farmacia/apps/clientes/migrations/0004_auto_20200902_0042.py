# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_remove_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='distrito',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='provincia',
        ),
    ]
