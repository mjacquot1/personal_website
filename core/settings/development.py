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

DEBUG = config("DEBUG_ENV", default=False, cast=bool)
# DEBUF = False

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
        # "OPTIONS": {
        #     "CLIENT_CLASS": "django_redis.client.DefaultClient"
        # },
    }
}

# # Dummy cache for local dev
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.dummy.DummyCache",
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CELERY_BROKER_URL = config(
    config("CELERY_BROKER_ENV"), default=config("REDIS_BACKEND_ENV"))
CELERY_RESULT_BACKEND = config(
    config("CELERY_BACKEND_ENV"), default=config("REDIS_BACKEND_ENV"))
CELERY_CACHE_BACKEND = 'default'

# Allows for uploading media like images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp', 'app_messages')

### Needed for debug toolbar ###
INTERNAL_IPS = [
    "127.0.0.1",
]

def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

### End for debug toolbar ###