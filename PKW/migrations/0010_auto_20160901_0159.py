# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PKW', '0009_district_last_edit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votingresult',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='votingresult',
            name='voivodeship',
        ),
        migrations.RemoveField(
            model_name='voivodeship',
            name='id',
        ),
        migrations.AlterField(
            model_name='voivodeship',
            name='Name',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='VotingResult',
        ),
    ]
