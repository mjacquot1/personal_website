"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import random
import string
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# three parents makes it go from 'settings' to 'core' to 'personal_website'
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# # (No longer) Render Deployment Code
# DEBUG = "DEBUG_ENV"  # Changed to just true. Used to be set up for render deployment.

# # Docker HOST
# ALLOWED_HOSTS = ['localhost']

# Add here your deployment HOSTS
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085']

# Probably not necessary since im not using render
# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
# if RENDER_EXTERNAL_HOSTNAME:
#     ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "home",
    "ui_testing",
    "bootstrap5",
    'theme_soft_design',
    'django_ses',
    'django_json_widget',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# HOME_TEMPLATES = os.path.join(BASE_DIR, 'home/', 'templates/')
# BASE_TEMPLATES = os.path.join(BASE_DIR, 'templates/')

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [HOME_TEMPLATES, BASE_TEMPLATES],
        "DIRS": [BASE_DIR / 'home' / 'templates', BASE_DIR / 'ui_testing' / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            'debug':True
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# # Database (Came with template)
# # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DB_ENGINE = os.getenv('DB_ENGINE', None)
# DB_USERNAME = os.getenv('DB_USERNAME', None)
# DB_PASS = os.getenv('DB_PASS', None)
# DB_HOST = os.getenv('DB_HOST', None)
# DB_PORT = os.getenv('DB_PORT', None)
# DB_NAME = os.getenv('DB_NAME', None)

# if DB_ENGINE and DB_NAME and DB_USERNAME:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.' + DB_ENGINE,
#             'NAME': DB_NAME,
#             'USER': DB_USERNAME,
#             'PASSWORD': DB_PASS,
#             'HOST': DB_HOST,
#             'PORT': DB_PORT,
#         },
#     }
# else:

# Update for postgres, Redis and celery

# SQL_ENGINE_ENV = django.db.backends.postgresql
# SQL_DATABASE_ENV = hello_django
# SQL_USER_ENV = hello_django
# SQL_PASSWORD_ENV = hello_django
# SQL_HOST_ENV = db
# SQL_PORT_ENV = 5432

# CELERY_BROKER_ENV = redis: // redis: 6379/0
# CELERY_BACKEND_ENV = redis: // redis: 6379/0

# # Redis Cache
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": config("REDIS_BACKEND"),
#     },
# }

# CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
# CELERY_RESULT_BACKEND = os.environ.get(
#     "CELERY_BACKEND", "redis://127.0.0.1:6379/0")

# Update for postgres and celery

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# if not DEBUG:
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = '/'
