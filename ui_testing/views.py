from django.shortcuts import render
from .models import Recreation, Web_Stack_Tools

# Create your views here.


def test_404(request):

    web_stack_tools = Web_Stack_Tools.objects.all().order_by('display_order')
    recreation_images = Recreation.objects.all().order_by('display_order')

    context = {
        'web_stack_tools': web_stack_tools,
        'recreation_images': recreation_images,
    }

    return render(request, 'resume.html', context)
