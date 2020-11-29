# Generated by Django 3.1.3 on 2020-11-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_auto_20201128_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_in_progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='back.profile')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.game_in_progress')),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.profile')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamers', to='back.team')),
            ],
        ),
        migrations.AddField(
            model_name='game_in_progress',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.game'),
        ),
    ]