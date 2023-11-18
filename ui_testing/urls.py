from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse, reverse_lazy

from . import views

app_name = 'ui_testing'

urlpatterns = [
    path('resume/', views.test_404, name='test_404'),
    path('demo/', views.demo, name='demo'),
]
