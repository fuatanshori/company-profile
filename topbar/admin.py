from django.contrib import admin
from .models import TopBar,Social
# Register your models here.

@admin.register(TopBar)
class TopBarAdmin(admin.ModelAdmin):
    pass


@admin.register(Social)
class Social(admin.ModelAdmin):
    pass