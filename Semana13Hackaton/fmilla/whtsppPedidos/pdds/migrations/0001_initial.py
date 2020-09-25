from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('documento', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='tipoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='tipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='tipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='transportista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('documento', models.CharField(max_length=15)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
                ('tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipodocumento')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('igv', models.BooleanField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
                ('tipoproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ubicacion', models.CharField(max_length=500)),
                ('estado', models.CharField(default='Recibido', max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.cliente')),
                ('transportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.transportista')),
            ],
        ),
        migrations.CreateModel(
            name='detallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.producto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipocliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipocliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipodocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipodocumento'),
        ),
    ]