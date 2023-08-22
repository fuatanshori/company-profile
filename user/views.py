from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.

def user_logout(request):
    logout(request)
    return redirect("companyprofile:index")