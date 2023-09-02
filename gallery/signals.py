from django.db.models.signals import post_save,post_delete,pre_save
from django.dispatch import receiver
from .models import Gallery,GalleryImage
@receiver(post_save, sender=Gallery)
def single_published_gallery(sender, instance, **kwargs):
    
    if instance.is_published:
        Gallery.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)   
    else:
        Gallery.objects.filter(is_published=False).exclude(pk=instance.pk).update(is_published=True)   
    
    publishes = Gallery.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_published)
    
    if all(not item for item in is_publishes):
        obj = Gallery.objects.get(pk=instance.pk)
        obj.is_published=True
        obj.save()

@receiver(post_delete,sender=Gallery)
def deleted_published_gallery(sender,instance,*args, **kwargs):
    if instance.is_published:
        obj = Gallery.objects.all().exclude(pk=instance.pk).first()
        obj.is_published=True
        obj.save()

