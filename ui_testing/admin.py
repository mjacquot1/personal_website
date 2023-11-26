from django.contrib import admin
from django.db import models
from django import forms
from django.forms.widgets import TextInput
from .models import Recreation, Web_Stack_Tools, ResumeSkillCategories, ResumeSkills, ResumeExperienceCategory, ResumeExperienceBlock, ResumeLine

from .forms import ResumeLineForm

from django_ses.views import DashboardView

# Register your models here.
class RecreationAdmin(admin.ModelAdmin):
    pass


class WebStackToolAdmin(admin.ModelAdmin):
    pass

class ResumeSkillCategoriesAdmin(admin.ModelAdmin):
    pass


class ResumeSkillsAdmin(admin.ModelAdmin):
    pass

class ResumeExperienceCategoryAdmin(admin.ModelAdmin):
    pass


class ResumeLineForm(forms.ModelForm):
    class Meta:
        model = ResumeExperienceBlock
        
        pass

class ResumeExperienceBlockAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.JSONField: {"widget": TextInput
    # },
    # }
    pass

class ResumeLineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Web_Stack_Tools, WebStackToolAdmin)
admin.site.register(Recreation, RecreationAdmin)
admin.site.register(ResumeSkillCategories, ResumeSkillCategoriesAdmin)
admin.site.register(ResumeSkills, ResumeSkillsAdmin)
admin.site.register(ResumeExperienceCategory, ResumeExperienceCategoryAdmin)
admin.site.register(ResumeExperienceBlock, ResumeExperienceBlockAdmin)
admin.site.register(ResumeLine, ResumeLineAdmin)