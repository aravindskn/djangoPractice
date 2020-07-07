"""
This module contains configuration settings for local environment.
"""

# pylint: disable=W0622
# pylint: disable=W0614
# pylint: disable=W0401'

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yj6o@&vrar6^l1u68!bxumj@xr4&5)zzk!h1qw&63^&@2d3w@#'

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
