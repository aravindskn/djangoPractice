"""
This module contains configuration settings for production environment.
"""

# pylint: disable=W0622
# pylint: disable=W0614
# pylint: disable=W0401

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#^9*y^t1kf4y*rut74hv1ao4bb#e@yc(n@0x^2032#48(vx*32'

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'aravindskn.pythonanywhere.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ftlabs',
        'TEST': {
            'NAME': 'test_ftlabs',
        },
        'USER': 'ftlabsdbadmin',
        'PASSWORD': 'ftlabsAdm3#n',
        'OPTIONS': {
            'autocommit': True,
        },
        'ATOMIC_REQUESTS': True
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/aravindskn/FullThrottleLabsTest/static'
