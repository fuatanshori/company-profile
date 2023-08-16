from django.db import models

# Create your models here.
class Intro(models.Model):
    title   = models.CharField(max_length=20)
    description = models.TextField(max_length=655)
    is_published = models.BooleanField(default=False)
    background_image = models.ImageField(upload_to='media/bgintro')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Intro'

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=655)
    image       = models.ImageField(upload_to='media/bgintro')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    class Meta:
        verbose_name_plural='About Us'

    def __str__(self):
        return self.title