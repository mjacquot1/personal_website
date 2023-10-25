from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse, reverse_lazy

from . import views

app_name = 'home'

# This is a placeholder to reroute all default views back to the homepage
homepage_view = RedirectView.as_view(url='/')

urlpatterns = [
    path('', views.index, name='index'),

    path('about-us-test/', homepage_view, name='about-us'),

    path('contact-us/', homepage_view, name='contact-us'),
    path('author/', homepage_view, name='author'),

    # Sections
    path('presentation/', homepage_view, name='presentation'),
    path('page-header/', homepage_view, name='page_header'),
    path('features/', homepage_view, name='features'),
    path('navbars/', homepage_view, name='navbars'),
    path('nav-tabs/', homepage_view, name='nav_tabs'),
    path('pagination/', homepage_view, name='pagination'),
    path('inputs/', homepage_view, name='inputs'),
    path('forms/', homepage_view, name='forms'),
    path('alerts/', homepage_view, name='alerts'),
    path('modals/', homepage_view, name='modals'),
    path('tooltips/', homepage_view, name='tooltips'),
    path('avatars/', homepage_view, name='avatars'),
    path('badges/', homepage_view, name='badges'),
    path('breadcrumbs/', homepage_view, name='breadcrumbs'),
    path('buttons/', homepage_view, name='buttons'),
    path('dropdowns/', homepage_view, name='dropdowns'),
    path('progress-bars/', homepage_view, name='progress_bars'),
    path('toggles/', homepage_view, name='toggles'),
    path('typography/', homepage_view, name='typography'),
]
