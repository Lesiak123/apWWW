# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Candidate(models.Model):
    Name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Name
    def clean(self):
        if Candidate.objects.count() > 1:
            raise ValidationError(_('Już jest dwóch kandydatów'))
    class Meta:
        ordering = ["Name"]


class Voivodeship(models.Model):
    Nr = models.IntegerField(default = 0)
    Name = models.CharField(max_length=200, primary_key=True)
    relevant_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Name


class District(models.Model):
    last_edit_date = models.DateField(_("Date"), default=datetime.now)
    voivodeship = models.ForeignKey(Voivodeship,on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    Inhabitants = models.IntegerField(default=0)
    eligible_voters = models.IntegerField(default=0)
    issued_ballots = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    relevant_votes = models.IntegerField(default=0)
    votes_for_first = models.IntegerField(default=0)
    def __str__(self):
        return self.Name


