from unipath import Path
import os
BASE_DIR = Path(__file__).ancestor(3)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SECRET_KEY = '6j5&!@q8m8s!)hxj%#m^a4im6xpu%r6qe5&!fywyu1@%&r_n3@'

DJANGO_APPS = (
    'suit',
    #'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    )

LOCAL_APPS = (
    'django.contrib.humanize',
    'apps.clientes',
    'apps.ventas',
    'apps.medicamentos',
    'apps.compras',
    'apps.distribuidor',  
    'apps.users',
    'apps.laboratorio',
    'apps.inline',
    'apps.factura',
   )

THIRD_PARTY_APPS = (

    )

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'farmacia.urls'
WSGI_APPLICATION = 'farmacia.wsgi.application'

#para personalizar admin con suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
          'django.core.context_processors.request',
)

AUTH_USER_MODEL = 'users.User'


LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'