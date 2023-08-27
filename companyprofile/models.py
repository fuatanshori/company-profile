from django.db import models


     

class About(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField(max_length=655)
    visi            = models.TextField()
    misi            = models.TextField()
    image           = models.ImageField(upload_to='media/aboutus')
    is_published    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=False)
    
    class Meta:
        verbose_name_plural='About'

    def __str__(self):
        return self.title
    
class MenuServices(models.Model):
    title_menu          = models.CharField(max_length=50)
    icon                = models.CharField(max_length=40)
    description_menu    = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)

    class Meta:
        verbose_name_plural = "MenuServices"

    def __str__(self):
        return self.title_menu
    
class Services(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField(max_length=400)
    menu_services   = models.ManyToManyField(MenuServices)
    is_published    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True,editable=False)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Email(models.Model):
    name        = models.CharField(max_length=100)
    email       = models.EmailField()
    subject     = models.CharField(max_length=100)
    message     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name