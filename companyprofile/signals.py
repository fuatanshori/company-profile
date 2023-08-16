from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Intro,AboutUs

@receiver(post_save, sender=Intro)
def single_published_intro(sender, instance, **kwargs):
    if instance.is_published:
        Intro.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)

@receiver(post_save, sender=AboutUs)
def single_published_intro(sender, instance, **kwargs):
    if instance.is_published:
        AboutUs.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)
