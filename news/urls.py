from django.urls import path
from . import views
urlpatterns = [
    path('',views.news,name='news'),
    path('news-detail/<str:id>/',views.newsDetail,name='news-detail'),
    path('news-admin-preview/',views.newsAdminPreview,name='news-admin-preview'),
    path('news-detail-admin-preview/<str:id>/',views.newsDetailAdminPreview,name='news-detail-admin-preview'),
]
