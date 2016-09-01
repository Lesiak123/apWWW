# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PKW', '0003_candidate_nr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voivodeship',
            name='relevant_votes',
        ),
    ]
