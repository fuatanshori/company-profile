from django.db import models

# Create your models here.
class About(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField(max_length=655)
    visi            = models.TextField()
    misi            = models.TextField()
    image           = models.ImageField(upload_to='media/about')
    is_active    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=False)
    
    class Meta:
        verbose_name_plural='About'

    def __str__(self):
        return self.title