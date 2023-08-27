from django.db import models
from PIL import Image
# Create your models here.

class GalleryImage(models.Model):
    gallery_name     = models.CharField(max_length=20)
    gallery_image   = models.ImageField(upload_to='media/gallery')
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery_name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.gallery_image:
            img = Image.open(self.gallery_image.path)
            new_dimensions = (1200, 900)
            img = img.resize(new_dimensions)
            img.save(self.gallery_image.path)

class Gallery(models.Model):
    title           = models.CharField(max_length=30)
    description     = models.TextField()
    image           = models.ManyToManyField(GalleryImage)
    is_published    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
