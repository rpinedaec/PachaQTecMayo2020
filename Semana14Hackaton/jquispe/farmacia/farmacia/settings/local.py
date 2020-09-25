from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'bdfarmacia.sqlite3',
    }
}

TEMPLATE_DIRS=(BASE_DIR, 'templates')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')