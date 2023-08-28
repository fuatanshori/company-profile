from django.urls import path
from . import views
urlpatterns = [
    path('',views.news,name='news'),
    path('detail/',views.newsdetail,name='news-detail'),
]
