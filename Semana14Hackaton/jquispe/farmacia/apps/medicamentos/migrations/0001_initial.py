# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10)),
                ('tipo', models.CharField(max_length=30, choices=[(b'generico', b'Generico'), (b'comercial', b'Comercial')])),
                ('nombre', models.CharField(unique=True, max_length=200)),
                ('componente', models.CharField(max_length=200)),
                ('concentracion', models.CharField(max_length=50)),
                ('sanitario', models.CharField(max_length=200)),
                ('fecha_expiracion', models.DateTimeField()),
                ('fecha_produccion', models.DateTimeField()),
                ('descripcion', models.TextField(max_length=400)),
                ('precio_Compra', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('precio_venta', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('stock', models.PositiveSmallIntegerField()),
                ('categoria', models.ForeignKey(to='medicamentos.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
