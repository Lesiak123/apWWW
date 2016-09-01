# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Candidate,Voivodeship,District
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Voivodeship)
admin.site.register(District)
