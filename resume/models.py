from typing import Any
from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.db.models.functions import (ExtractYear, ExtractMonth,)
from django.core.exceptions import ValidationError
from django.db.models import F

from .utils import ResumeLineHandler, enforce_display_order

# Create your models here.
class WebStackTools(models.Model):
    tool_name = models.CharField(max_length=30)
    tool_description = models.CharField()
    tool_link = models.URLField()

    main_image = models.ImageField(upload_to="web_stack_icons")
    display_order = models.IntegerField()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(WebStackTools, self).__init__(*args, **kwargs)
        self.__original_display_order = self.display_order

    def __str__(self):
        return f"{ self.tool_name }"
    
    def save(self, *args, **kwargs):
        # modify display order of other records
        enforce_display_order(self, self.__original_display_order, self.display_order)

        return super(WebStackTools, self).save(*args, **kwargs)
    
    # The larger of the width or height should be 64, and make the smaller size proportional
    def thumbnail_width(self):
        photo=self.main_image
        if photo.height == 0 : photo.height == 1

        if photo.width >= photo.height:
            return 64
        else:
            return (64/photo.height*photo.width)
    
    def thumbnail_height(self):
        photo=self.main_image
        if photo.width == 0 : photo.width == 1

        if photo.height >= photo.width:
            return 64
        else:
            return (64/photo.width*photo.height)
        
        
class ResumeSkillCategories(models.Model):
    category = models.CharField(max_length=50)
    display_order = models.IntegerField()

    # Display text for the view
    category_display = models.CharField()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ResumeSkillCategories, self).__init__(*args, **kwargs)
        self.__original_display_order = self.display_order

    def __str__(self):
        return f"{self.category}"
    
    def save(self, *args, **kwargs):
        # modify display order of other records
        enforce_display_order(self, self.__original_display_order, self.display_order)

        return super(ResumeSkillCategories, self).save(*args, **kwargs)


class ResumeSkills(models.Model):
    skill_title = models.CharField(max_length=30)
    skill_category = models.ForeignKey(ResumeSkillCategories, on_delete=models.PROTECT)
    skill_years = models.FloatField(default = 0)

    # This is what will be used to filter resume items
    skill_filter_category = models.CharField(max_length=30)

    # Override save field to make sure the title is lowercase
    def save(self, *args, **kwargs):
        self.skill_title = self.skill_title.upper()
        return super(ResumeSkills, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.skill_title}"
    
class ResumeExperienceCategory(models.Model):
    category = models.CharField(max_length=50)
    display_order = models.IntegerField(default = 0)

    # Display text for the view
    category_display = models.CharField()

    # Bootstrap icon to be displayed next to category
    icon_class = models.CharField(max_length=30, default='')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ResumeExperienceCategory, self).__init__(*args, **kwargs)
        self.__original_display_order = self.display_order

    def save(self, *args, **kwargs):
        # modify display order of other records
        enforce_display_order(self, self.__original_display_order, self.display_order)

        self.category = self.category.upper()
        self.category_display = self.category_display.upper()
        return super(ResumeExperienceCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.category}"
    
class ResumeExperienceBlock(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    sub_text = models.CharField(max_length=100, blank=True)

    start_date = models.DateField()
    end_date = models.DateField()
    still_there = models.BooleanField()

    category = models.ForeignKey(ResumeExperienceCategory, on_delete=models.PROTECT, default=None)

    lines = models.JSONField(default=dict)
    aggregate_line_skills = models.CharField(default='', blank=True)

    def save(self, *args, **kwargs):
        # Validate the format of the json information in skills
        # If invalid return error message
        resume_line_handler = ResumeLineHandler(self.lines)
        invalid_resume_lines = resume_line_handler.enforce_schema()
        if invalid_resume_lines: raise ValidationError(invalid_resume_lines)
        
        # Set something to state that the end date must be after the start date
        if self.start_date >= self.end_date: raise ValidationError("Start date cannot be at or before end date.")
        
        self.title = self.title.upper()

        # Make an easy to access string of aggregate skills
        # If there are no lines or skills, set to blank string
        aggregate_skills = resume_line_handler.return_aggregate_skills_set()
        self.aggregate_line_skills =  ' '.join(aggregate_skills) if aggregate_skills else ''

        if self.company: self.company = self.company.upper()

        return super(ResumeExperienceBlock, self).save(*args, **kwargs)
    
    def start_date_text(self):
        month = datetime.strftime(self.start_date, '%B')
        year = datetime.strftime(self.start_date, '%Y')
        return f"{month}, {year}"
    
    def end_date_text(self):
        month = datetime.strftime(self.end_date, '%B')
        year = datetime.strftime(self.end_date, '%Y')
        return f"{month}, {year}"
    
    def __str__(self):
        return f"{self.title} @ {self.company}"

class Recreation(models.Model):

    recreation_filters = {
    ("filter_mountain","Mountain"),
    ("filter_ocean","Ocean"),
    ("filter_art","Art"),
    ("filter_misc","Misc")
    }

    image_name = models.CharField(max_length=30)
    image_title = models.CharField(max_length=30)
    image_description = models.CharField()
    display_order = models.IntegerField(default = 0)

    filter_field = models.CharField(default="", choices=recreation_filters)

    main_image = models.ImageField(upload_to="recreation")
    tile_image = models.ImageField(upload_to="recreation")

    class meta:
        ordering = ['-display_order']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Recreation, self).__init__(*args, **kwargs)
        self.__original_display_order = self.display_order

    def save(self, *args, **kwargs):
        # modify display order of other records
        enforce_display_order(self, self.__original_display_order, self.display_order)

        return super(Recreation, self).save(*args, **kwargs)

    def __str__(self):
        return f"image: {self.image_name}\ntitle: {self.image_title}\ndescription: {self.image_description}"
    