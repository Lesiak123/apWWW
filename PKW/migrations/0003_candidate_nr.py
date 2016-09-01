# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PKW', '0002_remove_candidate_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='Nr',
            field=models.IntegerField(default=1),
        ),
    ]
