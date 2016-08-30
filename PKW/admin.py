from django.contrib import admin

from .models import Candidate,Voivodeship,VotingResult,District
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Voivodeship)
admin.site.register(VotingResult)
admin.site.register(District)