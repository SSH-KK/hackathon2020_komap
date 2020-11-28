# Generated by Django 3.1.3 on 2020-11-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_type', models.CharField(choices=[('QR', 'QR Code'), ('GPS', 'GPS Coordinates')], max_length=20)),
                ('name', models.CharField(max_length=150)),
                ('coordinates_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('coordinates_lon', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('description', models.TextField()),
                ('next_checkpoint_id', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('qr_data', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('average_time', models.DecimalField(decimal_places=0, max_digits=4)),
                ('lenght', models.DecimalField(decimal_places=0, max_digits=6)),
                ('co_op', models.BooleanField()),
                ('max_gamers', models.DecimalField(decimal_places=0, max_digits=3)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]