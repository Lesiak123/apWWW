# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_edit_date', models.DateField(default=datetime.datetime.now, verbose_name='Date')),
                ('Name', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=20)),
                ('Inhabitants', models.IntegerField(default=0)),
                ('eligible_voters', models.IntegerField(default=0)),
                ('issued_ballots', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('relevant_votes', models.IntegerField(default=0)),
                ('votes_for_first', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voivodeship',
            fields=[
                ('Nr', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('relevant_votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='voivodeship',
            field=models.ForeignKey(to='PKW.Voivodeship'),
        ),
    ]
