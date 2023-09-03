from django.db import models

# Create your models here.
class Social(models.Model):
    social_name = models.CharField(max_length=30)
    icon_name   = models.CharField(max_length=25)
    link        = models.CharField(max_length=400)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.social_name
    
class TopBar(models.Model):
    email           = models.EmailField()
    phone_number    = models.CharField(max_length=15,blank=True,null=True)
    social          = models.ManyToManyField(Social)
    is_active       = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    