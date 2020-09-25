# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0004_detallefactura_medicamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallefactura',
            old_name='medicamento',
            new_name='producto',
        ),
    ]
