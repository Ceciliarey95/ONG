from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql',
        'NAME'    : 'd94jbupvd88gms',
        'USER'    : 'gsilccgiowbhtk',
        'PASSWORD': '24231c3ee4697f9fed435a4d415d3fd0cf275acf8cb71a10dc1082216d7e8499',
        'HOST'    : 'ec2-44-206-197-71.compute-1.amazonaws.com',
        'PORT'    : '5432',
    }
}


import django_heroku
django_heroku.settings(locals())