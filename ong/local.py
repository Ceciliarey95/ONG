from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'ongdb',
        'USER'    : 'root',
        'PASSWORD': 'root',
        'HOST'    : 'localhost',
        'PORT'    : '',
    }
}