from django.contrib import admin
from .models import Recreation, Web_Stack_Tools

# Register your models here.
class RecreationAdmin(admin.ModelAdmin):
    pass


class WebStackToolAdmin(admin.ModelAdmin):
    pass


admin.site.register(Web_Stack_Tools, WebStackToolAdmin)
admin.site.register(Recreation, RecreationAdmin)