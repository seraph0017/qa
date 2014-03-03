"""
Django settings for qa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

selfpath = os.path.split(os.path.realpath(__file__))[0]
PATH = os.path.abspath(os.path.join(selfpath,'..'))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV = os.getenv('ENV')


if ENV in ['DEBUG','DEV']:
    isdebug = True
    STATIC_ROOT = ''
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),

)
else:
    STATIC_ROOT = PATH + '/static'
    STATICFILES_DIRS = ()
    isdebug = False

# import django_comments




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ul55o_%ki$enm$e!a-2*0%=%dfckkc2r6v1*!qq+@h=%zc3o0h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = isdebug

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = '*'


# login required
LOGIN_URL = r'/'

# by max 20140103

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.core.context_processors.request",
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'django.contrib.sites',
    'django_comments',
    # 'my_comment_app',




    # 'south',
    'account',
    'bbs',
    'django_gravatar',
    # 'lettuce.django',



    'pagination',
)

# COMMENTS_APP = 'my_comment_app'

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'qa.urls'

WSGI_APPLICATION = 'qa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qa',
        'USER': 'root',
        'PASSWORD': 'x09083412',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_ROOT
# static files
# by max 2013 12 22
STATICFILES_DIRS = STATICFILES_DIRS

# Templates files
# by max 2013 12 21
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates','bbs'),
]

# by max
AUTH_PROFILE_MODULE = 'account.UserProfile'

