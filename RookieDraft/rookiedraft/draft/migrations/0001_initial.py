# Generated by Django 3.0.6 on 2020-05-24 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueId', models.IntegerField()),
                ('teams', models.IntegerField(default=10)),
                ('rounds', models.IntegerField(default=4)),
                ('draft_order', models.CharField(max_length=500)),
                ('curr_round', models.IntegerField()),
                ('curr_pick', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.League')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=5)),
                ('position', models.CharField(max_length=5)),
                ('projection', models.IntegerField()),
                ('points', models.IntegerField()),
                ('drafted', models.BooleanField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.League')),
            ],
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('number', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.League')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='draft.Player')),
            ],
        ),
    ]
