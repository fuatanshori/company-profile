from django.shortcuts import render,redirect
from .models import About,Services,Email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from intro.models import Intro


# Create your views here.
def index(request):
    intro = Intro.objects.get(is_published=True)
    about = About.objects.get(is_published=True)
    services = Services.objects.get(is_published=True)
    context = {
        'intro_title':intro.title,
        'intro_description':intro.description,
        'intro_background_images':intro.background_image.all(),

        'about_title':about.title,
        'about_description':about.description,
        'about_visi':about.visi,
        'about_misi':about.misi,
        'about_image':about.image,
        
        'service_title':services.title,
        'service_description':services.description,
        'service_menu_services':services.menu_services.all(),

    }
    return render(request,'companyprofile/index.html',context)

def send_email(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        _message = request.POST['message']      
        try:
            mail_subject = 'Balasan Dari Instansi'
            message = render_to_string("companyprofile/email/contact.html",{
                "name":name
            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
        except :
            return redirect("companyprofile:index")
    return redirect("companyprofile:index")
