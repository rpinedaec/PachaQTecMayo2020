# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=40)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('cantidad', models.IntegerField()),
                ('impuesto', models.DecimalField(max_digits=6, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.IntegerField()),
                ('numero', models.CharField(max_length=6)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('vendedor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=5)),
                ('number', models.IntegerField()),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=300, null=True, blank=True)),
                ('imagen', models.ImageField(upload_to=b'productos', null=True, verbose_name=b'productos', blank=True)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('afecto', models.BooleanField(default=False)),
                ('igv', models.DecimalField(max_digits=6, decimal_places=2)),
                ('stock', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(blank=True, to='factura.CategoriaProducto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='factura',
            unique_together=set([('serie', 'numero')]),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(to='factura.Factura', db_column=b'factura_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(to='factura.Producto', db_column=b'producto_id'),
            preserve_default=True,
        ),
    ]
