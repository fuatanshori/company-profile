from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields=['created_at']
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ['is_published']
        return self.readonly_fields