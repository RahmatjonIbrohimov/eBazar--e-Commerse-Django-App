from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, post_delete
from django.contrib.auth.models import User

from .models import CreateAccount

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CreateAccount.objects.crete(user=instance)
        instance.save()

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    instance.profile.delete()
    print("Profile deleted")

