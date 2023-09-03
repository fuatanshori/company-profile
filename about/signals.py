from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import About
@receiver(post_save, sender=About)
def single_published_about(sender, instance, **kwargs):
    if instance.is_active:
        About.objects.filter(is_active=True).exclude(pk=instance.pk).update(is_active=False)   
    else:
        About.objects.filter(is_active=False).exclude(pk=instance.pk).update(is_active=True)   

    publishes = About.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_active)
    
    if all(not item for item in is_publishes):
        obj = About.objects.get(pk=instance.pk)
        obj.is_active=True
        obj.save()
    
@receiver(post_delete,sender=About)
def deleted_published_about(sender,instance,*args, **kwargs):
    if instance.is_active:
        obj = About.objects.all().exclude(pk=instance.pk).first()
        obj.is_active=True
        obj.save()