from django.shortcuts import render
from .models import News
from .utils import pagination_news
from django.http import Http404

# Create your views here.
def news(request):
    print(request.path)
    crousel = News.objects.filter(is_publish=True).order_by('-created_at')[:3]
    newss = News.objects.filter(is_publish=True).order_by('-created_at')
    custom_range,newss, = pagination_news(request,newss,6)
    context={
        'crousels':crousel,
        'newss':newss,
        'custom_range':custom_range,
    }
    return render(request,'news/news.html',context)



def newsDetail(request,id):
    try:
        news = News.objects.get(is_publish=True,id=id)
        context = {
            "news":news
        }
        return render(request,'news/detail_news.html',context)
    except News.DoesNotExist:
        raise  Http404 



def newsAdminPreview(request):
    if request.user.has_perm("news.can_preview_news"):
        crousel = News.objects.all().order_by('-created_at')[:3]
        newss = News.objects.all().order_by('-created_at')
        custom_range,newss, = pagination_news(request,newss,6)
        context={
            'crousels':crousel,
            'newss':newss,
            'custom_range':custom_range,
        }
        return render(request,'news/news.html',context)
    else:
        raise Http404

def newsDetailAdminPreview(request,id):
    if request.user.has_perm("news.can_preview_news"):
        news = News.objects.get(id=id)
        context = {
            "news":news
        }
        return render(request,'news/detail_news.html',context)
    else:
        raise Http404