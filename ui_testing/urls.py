from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse, reverse_lazy

from . import views

app_name = 'ui_testing'

urlpatterns = [
    path('', views.test_404, name='test_404'),
    # path('ignore_again/', views.test_404, name='ignore'),
]
