from django.shortcuts import render
from intro.models import Intro
from about.models import About
from services.models import Services
from gallery.models import Gallery
from contact.models import Contact
from contact.maps import maps_location
from .utils import get_data_or_none


def index(request):
    intro       = get_data_or_none(Intro)
    about       = get_data_or_none(About)
    services    = get_data_or_none(Services)
    gallery     = get_data_or_none(Gallery)
    contact     = get_data_or_none(Contact)
    print(request.path)

    context = {
        'intro_title': intro.title if intro else 'PLN Nusantara Power',
        'intro_description': intro.description if intro else 'Data Kosong',
        'intro_images': intro.image.all() if intro else '',

        'about_title': about.title if about else 'About',
        'about_description': about.description if about else 'Deskripsi About Masih Kosong',
        'about_visi': about.visi if about else ' Visi Kosong Silahkan isi Terlebih Dahulu',
        'about_misi': about.misi if about else 'Misi Kosong Silahkan isi Terlebih Dahulu',
        'about_image': about.image if about else '',

        'service_title': services.title if services else 'Service',
        'service_description': services.description if services else 'Deskripsi Kosong',
        'service_menu_services': services.menu_services.all() if services else '',

        'gallery_title': gallery.title if gallery else 'Gallery',
        'gallery_description': gallery.description if gallery else 'Deskripsi Kosong',
        'gallery_images': gallery.image.all() if gallery else '',

        'contact_title': contact.title if contact else 'Contact',
        'contact_description': contact.description if contact else 'Deskripsi Kosong',
        'contact_address': contact.address if contact else 'Alamat Masih Kosong',
        'contact_phone_number': contact.phone_number if contact else None,
        'contact_email': contact.email if contact else 'Email Masih Kosong',
        'contact_maps': contact.maps if contact else maps_location,

        

    }

    return render(request, 'plnnusantarapower/index.html', context)
