from django.shortcuts import render
from .models import Recreation, Web_Stack_Tools
from django.core.mail import send_mail

# Create your views here.


def test_404(request):

    display_html = 'resume.html'

    web_stack_tools = Web_Stack_Tools.objects.all().order_by('display_order')
    recreation_images = Recreation.objects.all().order_by('display_order')

    context = {
        'web_stack_tools': web_stack_tools,
        'recreation_images': recreation_images,
    }

    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message_body = request.POST['message-body']

        send_mail(
            message_name,
            (message_subject + '/' + message_body),
            message_email,
            ['mjacquot.dev@gmail.com']
        )

        context['message_name'] = message_name

        return render(request, display_html, context)

    else:
        return render(request, display_html, context)
