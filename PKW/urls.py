# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'PKW'

urlpatterns = [
    url(r'^viewing/inhabitants', views.editing_byinh),
    url(r'^viewing/voivodeships', views.editing_byvoiv),
    url(r'^viewing/type', views.editing_bytype),
    url(r'^viewing/save', views.editing_save),
    url(r'^rest/districts/$', views.listDistricts),
    url(r'^rest/voivodeships/$', views.listVoivodeships),
    url(r'^rest/candidates/$', views.listCandidates),
]
