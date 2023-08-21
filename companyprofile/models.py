from django.db import models
from .validatiors  import validate_aspect_ratio_1920_900
# Create your models here.
class Intro(models.Model):
    title               = models.CharField(max_length=20)
    description         = models.TextField(max_length=655)
    is_published        = models.BooleanField(default=False)
    background_image    = models.ImageField(upload_to='media/bgintro',validators=[validate_aspect_ratio_1920_900])
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Intro'

    def __str__(self):
        return self.title

     
class AboutUs(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField(max_length=655)
    image           = models.ImageField(upload_to='media/aboutus')
    is_published    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    class Meta:
        verbose_name_plural='About Us'

    def __str__(self):
        return self.title
    
class MenuServices(models.Model):
    title_menu          = models.CharField(max_length=30)
    icon                = models.CharField(max_length=40)
    description_menu    = models.CharField(max_length=130)
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "MenuServices"

    def __str__(self):
        return self.title_menu
    
class Services(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField(max_length=400)
    menu_services   = models.ManyToManyField(MenuServices)
    is_published    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
