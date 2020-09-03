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
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=100)),
                ('distrito', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('departamento', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(verbose_name=b'Telefono')),
                ('users', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
