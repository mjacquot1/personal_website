from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def resume(request):
    return render(request, 'pages/resume.html')


def index(request):

    # Page from the theme
    return render(request, 'pages/index.html')


def about_us(request):
    return render(request, 'pages/about-us.html')
