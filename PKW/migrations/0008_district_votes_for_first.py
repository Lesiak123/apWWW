# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-09 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PKW', '0007_district_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='votes_for_first',
            field=models.IntegerField(default=0),
        ),
    ]
