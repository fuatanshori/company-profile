from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Intro

@receiver(post_save, sender=Intro)
def single_published_intro(sender, instance, **kwargs):
    if instance.is_published:
        Intro.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)   
    else:
        Intro.objects.filter(is_published=False).exclude(pk=instance.pk).update(is_published=True)   

    publishes = Intro.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_published)
    
    if all(not item for item in is_publishes):
        obj = Intro.objects.get(pk=instance.pk)
        obj.is_published=True
        obj.save()
    
@receiver(post_delete,sender=Intro)
def deleted_published_intro(sender,instance,*args, **kwargs):
    if instance.is_published:
        obj = Intro.objects.all().exclude(pk=instance.pk).first()
        obj.is_published=True
        obj.save()