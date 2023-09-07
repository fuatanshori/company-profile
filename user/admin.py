from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.'

@admin.register(User)
class AdminUser(UserAdmin):
    readonly_fields=["date_joined","last_login"]
    list_display_links=["email","username"]
    list_display=["email","username","full_name","is_active","is_superuser","date_joined"]
    search_fields=["email","username"]
    ordering =["-date_joined"]
    filter_horizontal=[]
    list_filter=[]
    fieldsets = []
    
    add_fieldsets=[
        (
            None,{
            "classes":("wide"),
            "fields":('email',"username",'full_name',"password1","password2")
        }
        ),
    ]

# from django.contrib.auth.models import Permission
# from django.contrib import admin
# admin.site.register(Permission)