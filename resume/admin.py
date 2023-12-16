from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models
from django import forms
from django.forms.widgets import TextInput
# from django_json_widget.widgets import JSONEditorWidget
from .models import Recreation, WebStackTools, ResumeSkillCategories, ResumeSkills, ResumeExperienceCategory, ResumeExperienceBlock
from django.contrib import messages

from django_ses.views import DashboardView
from django_json_widget.widgets import JSONEditorWidget

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


class ResumeExperienceBlockAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.JSONField: {'widget': JSONEditorWidget},
    }

    # Don't save if there is an error while saving
    # Display error message on failed save
    def save_model(self, request, obj, form, change):
        try:
            super(ResumeExperienceBlockAdmin, self).save_model(request, obj, form, change)
        except Exception as e:
            messages.set_level(request, messages.ERROR)
            messages.error(request, e)


admin.site.register(WebStackTools, WebStackToolAdmin)
admin.site.register(Recreation, RecreationAdmin)
admin.site.register(ResumeSkillCategories, ResumeSkillCategoriesAdmin)
admin.site.register(ResumeSkills, ResumeSkillsAdmin)
admin.site.register(ResumeExperienceCategory, ResumeExperienceCategoryAdmin)
admin.site.register(ResumeExperienceBlock, ResumeExperienceBlockAdmin)