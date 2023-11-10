from django.db import models

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