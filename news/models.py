from django.db import models
from uuid import uuid4

# Create your models here.
class News(models.Model):
    id                  = models.UUIDField(unique=True,default=uuid4,editable=False,primary_key=True)
    news_title          = models.CharField(max_length=100)
    author              = models.CharField(max_length=55)
    news_description    = models.TextField()
    news_image          = models.ImageField(upload_to='media/news',blank=True,null=True,default='static/assets/img/defaultnewskotak.png')
    is_publish          = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'
        permissions = [("can_publish_news", "Can Publish News"),("can_preview_news", "Can Preview News")]
    def __str__(self) -> str:
        return self.news_title
    


