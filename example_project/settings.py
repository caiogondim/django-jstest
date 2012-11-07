# coding: utf-8

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/myadminmedia/'

ROOT_URLCONF = 'example_project.urls'

INSTALLED_APPS = (
    'jstest',
    'myapp',
)
