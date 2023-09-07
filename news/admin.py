from django.contrib import admin
from .models import News
from django.utils.html import format_html

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    ordering=['-created_at']
    readonly_fields=['created_at','view_preview_link']
    fieldsets = [
        ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description','view_preview_link']}),
        ('Publish Status', {'fields': ['is_publish']}),
    ]
    def get_fieldsets(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish_news'):
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description','view_preview_link']}),
                ('Publish Status', {'fields': ['is_publish']}),
            ]
        else:
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description','view_preview_link']}),
            ]
        
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish_news'):
            return self.readonly_fields
        else:
            return self.readonly_fields + ['is_publish'] 
        

    def view_preview_link(self, obj):
        if obj.news_title:  # Cek apakah objek sudah memiliki title (artinya sudah tersimpan dalam database)
            return format_html(f'Lihat Preview <a href="/news/news-detail-admin-preview/{obj.id}/">Disini</a>')
        else:
            return "silahkan simpan terlebih dahulu"
    view_preview_link.short_description = 'Lihat Preview'