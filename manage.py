#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from settings import return_config_env_variables

def main():
    """Run administrative tasks."""
    # DJANGO_SETTINGS_MODULE_ENV is an env variable imported through decouple
    config = return_config_env_variables()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE_ENV")) 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
