from django.urls import path
from . import views
urlpatterns = [
    path('',views.news,name='news'),
    path('detail/<str:id>/',views.newsdetail,name='news-detail'),
]
