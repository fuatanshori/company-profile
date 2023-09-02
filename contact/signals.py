from django.db.models.signals import post_save,post_delete,pre_save
from django.dispatch import receiver
from .models import Contact
@receiver(post_save, sender=Contact)
def single_published_contact(sender, instance, **kwargs):
    
    if instance.is_published:
        Contact.objects.filter(is_published=True).exclude(pk=instance.pk).update(is_published=False)   
    else:
        Contact.objects.filter(is_published=False).exclude(pk=instance.pk).update(is_published=True)   
    
    publishes = Contact.objects.all()
    is_publishes=[]
    for publish in publishes:
        is_publishes.append(publish.is_published)
    
    if all(not item for item in is_publishes):
        obj = Contact.objects.get(pk=instance.pk)
        obj.is_published=True
        obj.save()

@receiver(post_delete,sender=Contact)
def deleted_published_contact(sender,instance,*args, **kwargs):
    if instance.is_published:
        obj = Contact.objects.all().exclude(pk=instance.pk).first()
        obj.is_published=True
        obj.save()

