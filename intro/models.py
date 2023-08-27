from django.db import models
from intro.validatiors  import validate_aspect_ratio_1920_900
# Create your models here.

class BackgroundImageIntro(models.Model):
    image_name  = models.CharField(max_length=30)
    image       = models.ImageField(upload_to='media/bgintro',validators=[validate_aspect_ratio_1920_900])
    created_at  = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='Background Image Intro'

    def __str__(self):
        return f"{self.image_name}"
    
class Intro(models.Model):
    title               = models.CharField(max_length=20)
    description         = models.TextField(max_length=655)
    is_published        = models.BooleanField(default=False)
    background_image    = models.ManyToManyField(BackgroundImageIntro)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)

    class Meta:
        verbose_name_plural='Intro'

    def __str__(self):
        return self.title