# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-05-26 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seednetwork', '0004_memberinfo_external_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberinfo',
            name='site_agreement',
            field=models.BooleanField(default=False),
        ),
    ]