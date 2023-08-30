from django.shortcuts import render
from .models import News
from .utils import pagination_news
# Create your views here.
def news(request):
    crousel = News.objects.filter(is_publish=True).order_by('-created_at')[:3]
    newss = News.objects.filter(is_publish=True).order_by('-created_at')
    custom_range,newss, = pagination_news(request,newss,2)
    context={
        'crousels':crousel,
        'newss':newss,
        'custom_range':custom_range,
    }
    return render(request,'news/news.html',context)

def newsdetail(request,id):
    news = News.objects.get(id=id)
    context = {
        "news":news
    }
    return render(request,'news/detail_news.html',context)
