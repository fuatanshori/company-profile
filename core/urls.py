"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import error_404_view
from django.views.static import serve
urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    path('',include(('plnnusantarapower.urls','plnnusantarapower'))),
    path('',include(('user.urls','user'))),
    path("i18n/", include("django.conf.urls.i18n")),
    path('news/',include(('news.urls','news'))),
]
urlpatterns+=[re_path(r'^(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), ]
handler404   = error_404_view
