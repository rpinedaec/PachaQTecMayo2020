# Generated by Django 3.0.8 on 2020-07-29 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcione', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.MetodoPago')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.Producto')),
            ],
        ),
    ]