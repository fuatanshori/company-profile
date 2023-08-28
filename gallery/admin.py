from typing import Any, Optional
from django.contrib import admin
from .models import GalleryImage,Gallery
# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['title','is_published','created_at']
    min_objects = 1
    actions = None
    readonly_fields=['created_at']
    
    def has_delete_permission(self, request, obj=None):   
        queryset = self.model.objects.all()
        if queryset.count() <= self.min_objects:
            return False
        else:
            return super().has_delete_permission(request, obj)
        

    def get_readonly_fields(self, request, obj=None):
        if obj is None: 
            return self.readonly_fields
        else:
            queryset = self.model.objects.all()
            if queryset.count() <= self.min_objects:
                return self.readonly_fields + ['is_published']
            else:
                return self.readonly_fields

from django.utils.translation import gettext_lazy as gl
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
        def get_form(self,request,obj=None,change=False,**kwargs):
            form = super().get_form(request, obj, change, **kwargs)
            form.base_fields["gallery_image"].help_text=gl("Rekomendasi Dengan Format 1200 x 900")
            return form