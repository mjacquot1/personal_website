# Import base settings to use
from .base import *

from decouple import Csv
from settings import return_config_env_variables

config = return_config_env_variables()

# SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice(string.ascii_lowercase)
                         for i in range(32))

DEBUG = config("DEBUG_ENV")

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

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("REDIS_BACKEND_ENV"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}

# static files gathered from 'collectstatic' will be saved in './staticfiles' folder and served in the '/static/' url
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')

CELERY_BROKER_URL = config(
    config("CELERY_BROKER_ENV"), default=config("REDIS_BACKEND_ENV"))
CELERY_RESULT_BACKEND = config(
    config("CELERY_BACKEND_ENV"), default=config("REDIS_BACKEND_ENV"))

# Allows for uploading media like images
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = config("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = config("AWS_SES_REGION_ENDPOINT")
