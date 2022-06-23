from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from allauth.socialaccount.signals import social_account_added
from .models import FB_User, GG_User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if (created):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(social_account_added)
def create_social_user(sender, instance, created, **kwargs):
    if (created):
        if (instance.account.provider == 'facebook'):
            FB_User.objects.create(user=request.user)
        else:
            GG_User.objects.create(user=request.user)


@receiver(social_account_added)
def save_social_account(sender, instance, **kwargs):
    instance.profile.save()
    if (instance.account.provider == 'facebook'):
        instance.FB_User.save()
    else:
        instance.GG_User.save()
