from django.db import models
from .maps import maps_location
# Create your models here.
class Contact(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField()
    address         = models.TextField()
    phone_number    = models.CharField(null=True,blank=True,max_length=15)
    email           = models.EmailField(blank=True,null=True)
    maps            = models.TextField(default=maps_location,blank=True,null=True)
    is_published    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__ (self)->str:
        return self.title