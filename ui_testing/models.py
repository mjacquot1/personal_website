from django.db import models
from datetime import datetime
from django.db.models.functions import (ExtractYear, ExtractMonth,)

# Create your models here.
class Web_Stack_Tools(models.Model):
    tool_name = models.CharField(max_length=30)
    tool_description = models.CharField()
    tool_link = models.URLField()
    display_order = models.IntegerField(default = 0)

    main_image = models.ImageField(upload_to="web_stack_icons")

    def __str__(self):
        return f"{ self.tool_name }"
    
    # The larger of the width or height should be 64, and make the smaller size proportional
    def thumbnail_width(self):
        photo=self.main_image
        if photo.width >= photo.height:
            return 64
        else:
            return (64/photo.height*photo.width)
    
    def thumbnail_height(self):
        photo=self.main_image
        if photo.height >= photo.width:
            return 64
        else:
            return (64/photo.width*photo.height)
        
class ResumeSkillCategories(models.Model):
    category = models.CharField(max_length=50)
    display_order = models.IntegerField(default = 0)

    # Display text for the view
    category_display = models.CharField()

    def __str__(self):
        return f"{self.category}"

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

    def save(self, *args, **kwargs):
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

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        if self.company: self.company = self.company.upper()

        # Set something to state that the end date must be after the start date

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

class ResumeLine(models.Model):
    summary_item = models.BooleanField()
    line_text = models.TextField()
    resume_experience_block = models.ForeignKey(ResumeExperienceBlock, on_delete=models.CASCADE)

    line_skill_categories = models.ManyToManyField(ResumeSkills, blank=True)
    
    display_order = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.display_order = ResumeLine.objects.all().count()

        return super(ResumeLine, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.resume_experience_block} @ {self.line_text}"

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

    def __str__(self):
        return f"image: {self.image_name}\ntitle: {self.image_title}\ndescription: {self.image_description}"
    
    class meta:
        ordering = ['-display_order']