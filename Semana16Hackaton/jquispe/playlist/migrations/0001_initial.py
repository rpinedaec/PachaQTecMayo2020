# Generated by Django 3.1.1 on 2020-09-14 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('idAlbum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.albun')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musicname', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('idPlaylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('idSong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.song')),
            ],
        ),
        migrations.AddField(
            model_name='albun',
            name='idSinger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.singer'),
        ),
    ]
