# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_auto_20151014_0011'),
        ('clientes', '0003_remove_cliente_user'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabecera_Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ruc', models.CharField(unique=True, max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(max_length=9)),
                ('list', models.ForeignKey(related_name=b'cabecera_Venta', to='ventas.Cabecera_Venta')),
                ('medicamento', models.ForeignKey(to='medicamentos.Medicamentos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='detalle_tickets',
            name='medicamento',
        ),
        migrations.RemoveField(
            model_name='detalle_tickets',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='medicamento',
        ),
        migrations.DeleteModel(
            name='Detalle_Tickets',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
