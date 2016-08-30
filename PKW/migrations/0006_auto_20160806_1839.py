# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-06 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PKW', '0005_auto_20160413_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Inhabitants', models.IntegerField(default=0)),
                ('eligible_voters', models.IntegerField(default=0)),
                ('issued_ballots', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('relevant_votes', models.IntegerField(default=0)),
                ('voivodeship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PKW.Voivodeship')),
            ],
        ),
        migrations.AlterModelOptions(
            name='votingresult',
            options={'ordering': ['candidate']},
        ),
    ]
