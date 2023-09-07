from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import LihatBerita
@receiver(post_save, sender=LihatBerita)
def single_published_lihatberita(sender, instance, **kwargs):
    if instance.is_active:
        LihatBerita.objects.filter(is_active=True).exclude(pk=instance.pk).update(is_active=False)   
    else:
        LihatBerita.objects.filter(is_active=False).exclude(pk=instance.pk).update(is_active=True)   

    publishes = LihatBerita.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_active)
    
    if all(not item for item in is_publishes):
        obj = LihatBerita.objects.get(pk=instance.pk)
        obj.is_active=True
        obj.save()
    
@receiver(post_delete,sender=LihatBerita)
def deleted_published_lihatberita(sender,instance,*args, **kwargs):
    if instance.is_active:
        obj = LihatBerita.objects.all().exclude(pk=instance.pk).first()
        obj.is_active=True
        obj.save()