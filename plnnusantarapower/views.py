from django.shortcuts import render
from intro.models import Intro
from about.models import About
from services.models import Services
from gallery.models import Gallery
# Create your views here.

def index(request):
    intro = Intro.objects.get(is_published=True)
    about = About.objects.get(is_published=True)
    services = Services.objects.get(is_published=True)
    gallery = Gallery.objects.get(is_published=True)
    context = {
        'intro_title':intro.title,
        'intro_description':intro.description,
        'intro_images':intro.image.all(),

        'about_title':about.title,
        'about_description':about.description,
        'about_visi':about.visi,
        'about_misi':about.misi,
        'about_image':about.image,
        
        'service_title':services.title,
        'service_description':services.description,
        'service_menu_services':services.menu_services.all(),
        
        'gallery_title':gallery.title,
        'gallery_description':gallery.description,
        'gallery_images':gallery.image.all(),

    }
    return render(request,'plnnusantarapower/index.html',context)
