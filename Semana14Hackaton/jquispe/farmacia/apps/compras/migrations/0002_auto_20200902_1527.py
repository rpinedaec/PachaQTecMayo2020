# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0001_initial'),
        ('laboratorio', '0001_initial'),
        ('distribuidor', '0001_initial'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabecera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('distribuidor', models.ForeignKey(to='distribuidor.Distribuidor')),
                ('laboratorio', models.ForeignKey(to='laboratorio.Laboratorio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(max_length=9)),
                ('compra', models.ForeignKey(to='compras.Cabecera')),
                ('medicamento', models.ForeignKey(to='medicamentos.Medicamentos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='distribuidor',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='laboratorio',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='medicamento',
        ),
        migrations.RemoveField(
            model_name='medicamento_compra',
            name='compra',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.RemoveField(
            model_name='medicamento_compra',
            name='producto',
        ),
        migrations.DeleteModel(
            name='medicamento_compra',
        ),
    ]
