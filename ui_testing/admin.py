from django.contrib import admin
from .models import Recreation

# Register your models here.
class RecreationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recreation, RecreationAdmin)