from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def pagination_news(request,news,results):
    page = request.GET.get('page')
    # ! memcah news model dengan jumlah tertentu setiap pagenya
    paginator = Paginator(news,results)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        page=1
        news = paginator.page(page)
    except EmptyPage:
        page= paginator.num_pages
        news = paginator.page(page)
    
    left_index = (int(page)-1)
    if left_index < 1:
        left_index = 1
    right_index = (int(page)+2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    custom_range =range(left_index,right_index)
    return custom_range,news