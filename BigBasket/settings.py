"""
Django settings for BigBasket project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd$re=gb2e8ov5^+m0y9pm22&uxua00n3@fg!rirr075w4v@2p='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BigBasketApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'BigBasket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "static", "templates"),os.path.join(BASE_DIR, "static","static","adminApp"),os.path.join(BASE_DIR, "static", "static","userApp")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BigBasket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL')
#     )
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#     #     'NAME': 'postgres://uzrdugdzjqmhir:4ed2b288e4c7150f85611d5f919ab6948b2809b082dfb624cfed5b73af4447fd@ec2-54-235-84-244.compute-1.amazonaws.com:5432/d5j21qulhv2f1s',                      # Or path to database file if using sqlite3.
#     #     # 'USER': 'root',                      # Not used with sqlite3.
#     #     # 'PASSWORD': 'root',                  # Not used with sqlite3.
#     #     #                                      # Set to empty string for localhost. Not used with sqlite3.
#     #     # 'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
#     #     # 'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     # }
# }
DATABASES = {}
DATABASES['default'] = dj_database_url.parse('postgres://uzrdugdzjqmhir:4ed2b288e4c7150f85611d5f919ab6948b2809b082dfb624cfed5b73af4447fd@ec2-54-235-84-244.compute-1.amazonaws.com:5432/d5j21qulhv2f1s')


AUTH_USER_MODEL = 'BigBasketApp.User'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static"),
    )
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'