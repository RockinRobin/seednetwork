# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-20 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seedlibrary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('plant_timing', models.CharField(blank=True, max_length=30)),
                ('lodging', models.CharField(blank=True, max_length=30)),
                ('lodging_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('disease', models.CharField(blank=True, max_length=150)),
                ('days_to_maturity', models.IntegerField(blank=True)),
                ('threshing', models.CharField(blank=True, max_length=150)),
                ('cold_hardiness', models.CharField(blank=True, max_length=150)),
                ('culinary_qualities', models.CharField(blank=True, max_length=150)),
                ('other_traits', models.CharField(blank=True, max_length=150)),
                ('external_field', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='seed',
            name='more_info',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='extendedview',
            name='parent_seed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seedlibrary.Seed'),
        ),
    ]
