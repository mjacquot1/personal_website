# Import base settings to use
from .base import *

from decouple import config, Csv

# SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice(string.ascii_lowercase)
                         for i in range(32))

DEBUG = config("DEBUG_ENV", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS_ENV", cast=Csv())

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("SQL_DATABASE_ENV"),
        "USER": config("SQL_USER_ENV"),
        "PASSWORD": config("SQL_PASSWORD_ENV"),
        "HOST": config("SQL_HOST_ENV"),
        "PORT": config("SQL_PORT_ENV", cast=int),
    }
}