# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_auto_20151014_0011'),
        ('ventas', '0005_auto_20151127_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(max_length=9)),
                ('list_id', models.ForeignKey(to='ventas.Cabecera_Venta')),
                ('medicamento', models.ForeignKey(to='medicamentos.Medicamentos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='list_id',
        ),
        migrations.DeleteModel(
            name='Detalle_Venta',
        ),
    ]
