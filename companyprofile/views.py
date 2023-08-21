from django.shortcuts import render
from .models import Intro,AboutUs,Services
# Create your views here.
def index(request):
    intro = Intro.objects.get(is_published=True)
    aboutus = AboutUs.objects.get(is_published=True)
    services = Services.objects.get(is_published=True)
    context = {
        'intro_title':intro.title,
        'intro_description':intro.description,
        'intro_background_image':intro.background_image,

        'aboutus_title':aboutus.title,
        'aboutus_description':aboutus.description,
        'aboutus_image':aboutus.image,
        
        'service_title':services.title,
        'service_description':services.description,
        'service_menu_services':services.menu_services,

    }
    return render(request,'companyprofile/index.html',context)