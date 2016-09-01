# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from .models import District, Voivodeship, Candidate


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ('last_edit_date', 'voivodeship', 'Name', 'Type', 'Inhabitants', 'eligible_voters', 'issued_ballots', 'votes', 'relevant_votes', 'votes_for_first')


class VoivodeshipSerializer(ModelSerializer):
    class Meta:
        model = Voivodeship
        fields = ('Nr', 'Name')


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('Name', 'Nr')
