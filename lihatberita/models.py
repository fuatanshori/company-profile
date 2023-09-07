from django.db import models

# Create your models here.
class LihatBerita(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    button_name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="Lihat Berita"
    def __str__(self):
        return self.title