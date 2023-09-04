from django.contrib import admin
from .models import News
from django.contrib.auth.models import Permission

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    ordering=['-created_at']
    readonly_fields=['created_at']
    fieldsets = [
        ('News Details', {'fields': ['news_title', 'author', 'news_description']}),
        ('Publish Status', {'fields': ['is_publish']}),
    ]
    def get_fieldsets(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish'):
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author', 'news_description']}),
                ('Publish Status', {'fields': ['is_publish']}),
            ]
        else:
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author', 'news_description']}),
            ]
        
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish'):
            return self.readonly_fields
        else:
            return self.readonly_fields + ['is_publish']  
