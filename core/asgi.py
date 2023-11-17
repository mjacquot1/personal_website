"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from settings import return_config_env_variables

config = return_config_env_variables()

# DJANGO_SETTINGS_MODULE_ENV is an env variable imported through decouple
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      config("DJANGO_SETTINGS_MODULE_ENV"))

application = get_asgi_application()
