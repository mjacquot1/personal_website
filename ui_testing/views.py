from django.shortcuts import render
# from .models import (
#     Recreation, Web_Stack_Tools, 
#     ResumeSkillCategories, ResumeSkills,
#     ResumeExperienceCategory, ResumeExperienceBlock, ResumeLine
#     )
        
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


from .utils import ResumeLineHandler

# Create your views here.
def test_404(request):
    pass

def demo(request):
    return render(request, 'demo7.html')
