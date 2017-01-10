"""
Django settings for yogesh_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


from unipath import Path
import os
import sys


PROJECT_DIR = Path(__file__).ancestor(3)
PROJECT_ROOT = Path(__file__).ancestor(2) # settings file directry


sys.path.insert(0, Path(PROJECT_ROOT, 'apps'))



SECRET_KEY = '_$vou=iicn9!@mm#gci3wfc(yug9%shz*ak&ar-ppozs6lh*_*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'google_analytics',
    'blogango',
    'pingback',
    'django_xmlrpc',
    'taggit',
    'django.contrib.comments',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yogesh_blog.urls'

WSGI_APPLICATION = 'yogesh_blog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'blog.db',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'



MEDIA_ROOT = PROJECT_DIR.child("media")

MEDIA_URL = '/media/'

STATIC_ROOT =  PROJECT_DIR.child("collected_static")

STATIC_URL = '/static/'


STATICFILES_DIRS = (

    PROJECT_DIR.child("static"),
)

TEMPLATE_DIRS = (
    PROJECT_ROOT.child("templates"),
    
)


SITE_ID = 1