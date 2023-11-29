"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from settings import return_config_env_variables

config = return_config_env_variables()

# DJANGO_SETTINGS_MODULE_ENV is an env variable imported through decouple
os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE_ENV")) 

application = get_wsgi_application()
