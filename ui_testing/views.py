from django.shortcuts import render
from .models import Recreation

# Create your views here.


def test_404(request):

    recreation_images = Recreation.objects.all()

    context = {
        'recreation_images': recreation_images
    }

    return render(request, 'resume.html', context)
