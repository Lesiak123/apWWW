# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PKW', '0003_auto_20160410_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='voivodeship',
            name='Nr',
            field=models.IntegerField(default=0),
        ),
    ]