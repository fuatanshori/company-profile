from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import About
@receiver(post_save, sender=About)
def single_published_about(sender, instance, **kwargs):
    if instance.is_published:
        About.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)   
    else:
        About.objects.filter(is_published=False).exclude(pk=instance.pk).update(is_published=True)   

    publishes = About.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_published)
    
    if all(not item for item in is_publishes):
        obj = About.objects.get(pk=instance.pk)
        obj.is_published=True
        obj.save()
    
@receiver(post_delete,sender=About)
def deleted_published_about(sender,instance,*args, **kwargs):
    if instance.is_published:
        obj = About.objects.all().exclude(pk=instance.pk).first()
        obj.is_published=True
        obj.save()