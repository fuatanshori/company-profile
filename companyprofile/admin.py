from django.contrib import admin
from .models import Intro,AboutUs

# Register your models here.
@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display=['title','is_published','created_at']
    readonly_fields=['created_at']

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['title','is_published','created_at']
    readonly_fields=['created_at']
 
