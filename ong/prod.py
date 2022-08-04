from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddlmb0rmuqa4ed',
        'USER': 'oujzvcyraeinci',
        'PASSWORD': '6efae2c768f9bd04fcc464a97f9a8e4d90751202eb82b97cbf63e7c54f9f4b49',
        'HOST': 'ec2-18-214-35-70.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


import django_heroku
django_heroku.settings(locals())