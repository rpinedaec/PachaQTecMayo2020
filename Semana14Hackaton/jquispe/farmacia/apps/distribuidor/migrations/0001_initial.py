# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(default=1, unique=True, max_length=10, blank=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=60)),
                ('rut', models.IntegerField(max_length=11)),
                ('direccion', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
