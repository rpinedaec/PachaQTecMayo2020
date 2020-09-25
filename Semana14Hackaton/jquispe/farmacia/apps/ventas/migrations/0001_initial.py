# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_auto_20151014_0011'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Tickets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(max_length=9)),
                ('medicamento', models.ForeignKey(to='medicamentos.Medicamentos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
                ('medicamento', models.ManyToManyField(to='medicamentos.Medicamentos', through='ventas.Detalle_Tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle_tickets',
            name='ticket',
            field=models.ForeignKey(to='ventas.Ticket'),
            preserve_default=True,
        ),
    ]
