from django.conf import settings
from django.shortcuts import render


def error_404_view(request, exception):
	return render(request, '404.html')
