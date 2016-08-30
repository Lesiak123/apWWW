from django.db.models.signals import pre_save
from django.dispatch import receiver
from PKW.models import Candidate

@receiver(pre_save, sender=Candidate)
def candidate_check(sender, **kwargs):
    if Candidate.objects.count() > 1:
        print("NIE DODAWAJ YO")