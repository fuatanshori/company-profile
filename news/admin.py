from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    ordering=['-created_at']
    readonly_fields=['created_at']
    fieldsets = [
        ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description']}),
        ('Publish Status', {'fields': ['is_publish']}),
    ]
    def get_fieldsets(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish_news'):
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description']}),
                ('Publish Status', {'fields': ['is_publish']}),
            ]
        else:
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description']}),
            ]
        
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish_news'):
            return self.readonly_fields
        else:
            return self.readonly_fields + ['is_publish'] 

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.has_perm('news.can_publish_news'):
            form.base_fields['is_publish'].help_text = f'<br>Lihat Preview <a href="/news/news-detail-admin-preview/{obj.id}/">Disini</a>'
            form.base_fields['news_description'].help_text = f'<br>Lihat Preview <a href="/news/news-detail-admin-preview/{obj.id}/">Disini</a>'
        else:
            form.base_fields['news_description'].help_text = f'<br>Lihat Preview <a href="/news/news-detail-admin-preview/{obj.id}/">Disini</a>'
        return form 
