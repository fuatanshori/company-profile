from django.shortcuts import render,HttpResponse
from intro.models import Intro
from about.models import About
from services.models import Services
from gallery.models import Gallery
from contact.models import Contact
# Create your views here.

def index(request):
    try:
        intro = Intro.objects.get(is_published=True)
        about = About.objects.get(is_published=True)
        services = Services.objects.get(is_published=True)
        gallery = Gallery.objects.get(is_published=True)
        contact = Contact.objects.get(is_published=True)
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

            'contact_title':contact.title,
            'contact_description':contact.description,
            'contact_address':contact.address,
            'contact_phone_number':contact.phone_number,
            'contact_email':contact.email,
            'contact_maps':contact.maps,

        }
        return render(request,'plnnusantarapower/index.html',context)
    except:

        context = {
            'intro_title':'PLN Nusantara Power',
            'intro_description':'',
            'intro_images':'',

            'about_title':'About',
            'about_description':'',
            'about_visi':'',
            'about_misi':'',
            'about_image':'',
            
            'service_title':'Service',
            'service_description':'',
            'service_menu_services':'',
            
            'gallery_title':'Gallery',
            'gallery_description':'',
            'gallery_images':'',

            'contact_title':'Contact',
            'contact_description':'',
            'contact_address':'',
            'contact_phone_number':None,
            'contact_email':'',
            'contact_maps':'',

        }
        return render(request,'plnnusantarapower/index.html',context)