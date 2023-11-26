from django import forms
from .models import ResumeSkills
    

class ResumeLineForm(forms.Form):
    resume_skills_list = [i.skill_filter_category for i in ResumeSkills.objects.all()]

    resume_line_text = forms.CharField(label="Resume Line Text")
    resume_line_skills = forms.MultipleChoiceField(choices=resume_skills_list, label="Select Related Skills", required=False)
    is_summary = forms.BooleanField(label="Is this a summary line?")

