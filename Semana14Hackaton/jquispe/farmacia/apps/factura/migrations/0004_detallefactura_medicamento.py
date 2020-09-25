# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_medicamentos_igv'),
        ('factura', '0003_auto_20151210_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallefactura',
            name='medicamento',
            field=models.ForeignKey(db_column=b'medicamento_id', default=1, to='medicamentos.Medicamentos'),
            preserve_default=False,
        ),
    ]
