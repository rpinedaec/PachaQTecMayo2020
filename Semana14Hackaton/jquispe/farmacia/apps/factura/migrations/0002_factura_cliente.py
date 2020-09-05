# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_remove_cliente_user'),
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(blank=True, to='clientes.Cliente', null=True),
            preserve_default=True,
        ),
    ]
