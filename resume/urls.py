from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse, reverse_lazy

from django.views.decorators.cache import cache_page

from . import views

app_name = 'resume'

urlpatterns = [
    # Cache seconds * minutes * hours (1 if none)
    path('', cache_page(10 * 1 * 1)(views.resume_main_page), name='resume_main_page'),
]
