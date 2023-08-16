from django.urls import path
from . import views
urlpatterns = [
    path('logout/',views.user_logout,name='logout')
]
