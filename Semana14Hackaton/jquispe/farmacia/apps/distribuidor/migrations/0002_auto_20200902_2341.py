# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distribuidor',
            old_name='rut',
            new_name='ruc',
        ),
    ]
