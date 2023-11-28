from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse, reverse_lazy

from . import views

app_name = 'ui_testing'

urlpatterns = [
    path('/', views.resume_main_page, name='resume_main_page'),
]
