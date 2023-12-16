from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import WebStackTools, ResumeSkillCategories, Recreation, ResumeExperienceCategory
from django.core.signals import request_finished

from .utils import enforce_display_order


# On delete of these model records, decrease the display order of all folowwing records by -1
@receiver(post_delete, sender=Recreation, dispatch_uid="enforce_Recreation_display_order_on_deletion")
@receiver(post_delete, sender=WebStackTools, dispatch_uid="enforce_WebStackTools_display_order_on_deletion")
@receiver(post_delete, sender=ResumeSkillCategories, dispatch_uid="enforce_ResumeSkillCategories_display_order_on_deletion")
@receiver(post_delete, sender=ResumeExperienceCategory, dispatch_uid="enforce_ResumeExperienceCategory_display_order_on_deletion")
def enforce_display_order_on_deletion(sender, instance, using, **kwargs):
    enforce_display_order(instance, getattr(instance, 'display_order', None), None)
