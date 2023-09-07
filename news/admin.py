from django.contrib import admin
from .models import News
from django.utils.html import format_html

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    ordering=['-created_at']
    readonly_fields=['created_at','news_detail_preview','news_perview']
    fieldsets = [
        ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description','news_detail_preview','news_perview']}),
        ('Publish Status', {'fields': ['is_publish']}),
    ]
    def get_fieldsets(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish_news'):
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description','news_detail_preview','news_perview']}),
                ('Publish Status', {'fields': ['is_publish']}),
            ]
        else:
            fieldsets = [
                ('News Details', {'fields': ['news_title', 'author','news_image', 'news_description','news_detail_preview','news_perview']}),
            ]
        
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        # Cek apakah pengguna memiliki izin can_publish
        if request.user.has_perm('news.can_publish_news'):
            return self.readonly_fields
        else:
            return self.readonly_fields + ['is_publish'] 
        

    def news_detail_preview(self, obj):
        if obj.news_title and obj.news_description and obj.created_at:  # Cek apakah objek sudah memiliki title (artinya sudah tersimpan dalam database)
            return format_html(f'Lihat Detail News Preview <a href="/news/news-detail-admin-preview/{obj.id}/">Disini</a>')
        else:
            return "silahkan simpan terlebih dahulu"
   
    def news_perview(self,obj):
        if obj.news_title and obj.news_description and obj.created_at:  # Cek apakah objek sudah memiliki title (artinya sudah tersimpan dalam database)
            return format_html(f'Lihat News Preview <a href="/news/news-admin-preview/">Disini</a>')
        else:
            return "silahkan simpan terlebih dahulu"
        
    news_detail_preview.short_description = 'Lihat Detail Preview'
    news_perview.short_description = 'Lihat News Preview'