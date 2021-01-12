# -*- coding: utf-8 -*-

"""
Django settings for djangodemo project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import environ
import os


# https://github.com/joke2k/django-environ
env = environ.Env(
    DEBUG=(bool, False),
    DEBUG_TOOLBAR_SHOW=(bool, False),
)
env_root = (environ.Path(__file__) - 3) # get root of the project
env_path = env_root() + '/conf/env_settings'
# print(env_path)
environ.Env.read_env(env_path)


# sentry - https://sentry.io/black-foundry/
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=env('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
	environment=env('SENTRY_ENVIRONMENT'),
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

ENV_DIR = os.path.dirname(BASE_DIR)
# print(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

JWT_SECRET = env('JWT_SECRET')
JWT_ALGORITHM = 'HS256'

TEST_API_HOST = env('TEST_API_HOST')
TEST_API_USERNAME = env('TEST_API_USERNAME')
TEST_API_PASSWORD = env('TEST_API_PASSWORD')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    '164.90.229.235', '.robocjk-development.black-foundry.com',
    '161.35.31.249', '.robocjk-production.black-foundry.com',
]

SITE_ID = 1

ADMINS = [
    ('Fabio Caccamo', 'fabio.caccamo@gmail.com', )
]

MANAGERS = [
    ('Fabio Caccamo', 'fabio.caccamo@gmail.com', )
]


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.sites',
    # 'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'corsheaders',
    'debug_toolbar',
    'django_json_widget',
    'robocjk',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'csp.middleware.CSPMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
            ],
        },
    },
]


# Session
# https://docs.djangoproject.com/en/dev/ref/settings/#sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = (1209600 * 26) # (2 weeks * 26 = 52 weeks, in seconds)'
# SESSION_COOKIE_DOMAIN = ''

DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

WSGI_APPLICATION = 'app.wsgi.application'

ROOT_URLCONF = 'app.urls'

APPEND_SLASH = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('fr', 'Français'),
    ('it', 'Italiano'),
)
MULTILANGUAGE = len(LANGUAGES) > 1

TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False


DATE_FORMAT = 'Y/m/d'
# DATETIME_FORMAT = 'Y/m/d H:i:s.u'
DATETIME_FORMAT = 'Y/m/d H:i:s'


# https://docs.djangoproject.com/en/3.1/ref/settings/#data-upload-max-memory-size
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440 * 4 # 10 MB

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = env('MEDIA_ROOT')

# Used for media served from CDN
MEDIA_HOST = env('MEDIA_HOST', default='')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = '/media/'
MEDIA_URL = MEDIA_HOST + '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = env('STATIC_ROOT')

STATIC_HOST = env('STATIC_HOST', default='')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'
STATIC_URL = STATIC_HOST + '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # VIRTUALENV_PATH +'/sources/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# if DEBUG:
#    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# else:
#    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': ENV_DIR + '/cache/',
    },
}


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# import logging
# logger = logging.getLogger('app')
# logger.debug('message')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(name)s [%(levelname)s]: %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s %(name)s %(module)s %(process)d %(thread)d [%(levelname)s]: %(message)s'
        },
    },
    'handlers': {
        'debug_file': {
            'level': 'DEBUG',
            # 'class': 'logging.FileHandler',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ENV_DIR + '/logs/django-debug.log',
            'maxBytes': 1024 * 1024 * 2, # 2 MB
            'backupCount': 5,
            'formatter':'simple',
        },
        'error_file': {
            'level': 'ERROR',
            # 'class': 'logging.FileHandler',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ENV_DIR + '/logs/django-errors.log',
            'maxBytes': 1024 * 1024 * 2, # 2 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['error_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'app': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'robocjk': {
            'handlers': ['debug_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


# django-cors-headers
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
)


# django-csp - https://django-csp.readthedocs.io/
CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", 'data:', 'blob:',
    # 'cdn.jsdelivr.net', 'use.fontawesome.com',
    '*.black-foundry.com',
    # '*.kxcdn.com',
    # '*.google.com', '*.googleapis.com', '*.gstatic.com',
    # '*.google-analytics.com', '*.doubleclick.net', '*.googletagmanager.com', '*.hotjar.com',
    # '*.youtube.com', '*.vimeo.com',
)


# django-debug-toolbar - https://pypi.python.org/pypi/django-debug-toolbar/
DEBUG_TOOLBAR_SHOW = env('DEBUG_TOOLBAR_SHOW')
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG_TOOLBAR_SHOW and DEBUG,
}
INTERNAL_IPS = ('127.0.0.1', )


# hashids - https://github.com/davidaurelio/hashids-python
HASHIDS_SALT = env('HASHIDS_SALT')
HASHIDS_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
HASHIDS_MIN_LENGTH = 7
HASHIDS_OPTIONS = {
    'salt': HASHIDS_SALT,
    'alphabet': HASHIDS_ALPHABET,
    'min_length': HASHIDS_MIN_LENGTH,
}
