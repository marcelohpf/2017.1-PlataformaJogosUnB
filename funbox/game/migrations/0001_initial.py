# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 13:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import game.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="What's the name of the game?", max_length=100, verbose_name='Game Name')),
                ('cover_image', models.ImageField(help_text='Accepted formats: png, jpg, jpeg, etc.', upload_to='images/', verbose_name='CoverImage')),
                ('game_version', models.CharField(blank=True, help_text="What's the game version?", max_length=20, null=True, validators=[game.validators.validate_version], verbose_name='Game Version')),
                ('official_repository', models.URLField(help_text='What is the official repository for this game?', validators=[django.core.validators.URLValidator()], verbose_name='Official Repository')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.FileField(help_text="Choose the game's package", upload_to='packages/', verbose_name='Package')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Name of the game's package", max_length=50, verbose_name='Platform name')),
                ('extensions', models.CharField(choices=[('deb', 'deb'), ('exe', 'exe'), ('rpm', 'rpm'), ('app', 'app')], default='deb', help_text='Select the package extension that will be accepted', max_length=3, verbose_name='Valid extension')),
                ('icon', models.FileField(upload_to='Platform', verbose_name='Platform Icon')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='platforms',
            field=models.ManyToManyField(related_name='platforms', to='game.Platform'),
        ),
    ]