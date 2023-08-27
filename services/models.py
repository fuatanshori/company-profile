from django.db import models

# Create your models here.
class MenuServices(models.Model):
    menu_title          = models.CharField(max_length=50)
    menu_icon           = models.CharField(max_length=40)
    menu_description    = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)

    class Meta:
        verbose_name_plural = "Menu Services"
    def __str__(self):
        return self.menu_title
    
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