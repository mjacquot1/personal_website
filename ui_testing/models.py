from django.db import models

# Create your models here.
class Recreation(models.Model):
    image_name = models.CharField(max_length=30)
    image_title = models.CharField(max_length=30)
    image_description = models.CharField()
    display_order = models.IntegerField(default = 0)

    main_image = models.ImageField(upload_to="recreation")
    tile_image = models.ImageField(upload_to="recreation")

    def __str__(self):
        return f"image: {self.image_name}\ntitle: {self.image_title}\ndescription: {self.image_description}"
    
    class meta:
        ordering = ['display_order']