from django.shortcuts import render
from .models import Intro
# Create your views here.
def index(request):
    intro = Intro.objects.get(is_published=True)
    context = {
        'title':intro.title,
        'description':intro.description,
        'background_image':intro.background_image,
    }
    return render(request,'companyprofile/index.html',context)