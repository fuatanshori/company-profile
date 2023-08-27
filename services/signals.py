from .models import Services
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Services)
def single_published_services(sender, instance, **kwargs):
    if instance.is_published:
        Services.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)   
    else:
        Services.objects.filter(is_published=False).exclude(pk=instance.pk).update(is_published=True)   
    
    publishes = Services.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_published)
    
    if all(not item for item in is_publishes):
        obj = Services.objects.get(pk=instance.pk)
        obj.is_published=True
        obj.save()

@receiver(post_delete,sender=Services)
def deleted_published_services(sender,instance,*args, **kwargs):
    if instance.is_published:
        obj = Services.objects.all().exclude(pk=instance.pk).first()
        obj.is_published=True
        obj.save()