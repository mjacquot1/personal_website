from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def home(request):
    response = redirect('/resume/')
    return response

def error(request):
    response = redirect('/resume/')
    return response
