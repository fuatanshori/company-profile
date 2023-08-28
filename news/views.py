from django.shortcuts import render

# Create your views here.
def news(request):
    print(request.path)
    return render(request,'news/news.html')

def newsdetail(request):
    return render(request,'news/detail_news.html')