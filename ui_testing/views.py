from django.shortcuts import render
from .models import Recreation, Web_Stack_Tools, ResumeSkillCategories, ResumeSkills
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
def test_404(request):

    display_html = 'resume.html'

    web_stack_tools = Web_Stack_Tools.objects.all().order_by('display_order')
    recreation_images = Recreation.objects.all().order_by('display_order')
    resume_skill_categories =  ResumeSkillCategories.objects.all().order_by('display_order')
    resume_skills = ResumeSkills.objects.all()

    resume_skills_categorized = {}

    ## Make a dictionary of 
    for skill in resume_skills:
        skill_category = skill.skill_category.category
        if skill_category in resume_skills_categorized.keys():
            resume_skills_categorized[skill_category].append(skill)
        else:
            resume_skills_categorized[skill_category] = [skill]

    context = {
        'web_stack_tools': web_stack_tools,
        'recreation_images': recreation_images,
        'debug' : settings.DEBUG,
        'resume_skill_categories' : resume_skill_categories,
        'resume_skills_categorized' : resume_skills_categorized,
    }

    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message_body = request.POST['message-body']

        # Alert Messages are saved in cookies first, then user session if needed.
        # Already protected from header injections.
        messages.add_message(request, messages.INFO, f'Thank you for reaching out {message_name}!')

        send_mail(
            message_name,
            (message_subject + '/' + message_body),
            'mjacquot.dev@gmail.com',
            ['mjacquot.dev@gmail.com'],
            fail_silently=False,
        )

        context['message_name'] = message_name

        return render(request, display_html, context)

    else:
        return render(request, display_html, context)
# Create your views here.
def demo(request):
    return render(request, 'demo7.html')
