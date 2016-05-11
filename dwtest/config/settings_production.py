from dwtest.config.settings_common import *
import os


## probably update this. probably.
ALLOWED_HOSTS = ['*']


########## DEBUG CONFIGURATION
DEBUG = False
########## END DEBUG CONFIGURATION







########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#POSTGRES example. Be sure to install: pip install psycopg2
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

########## END DATABASE CONFIGURATION

WSGI_APPLICATION = 'dwtest.wsgi.application'


STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

#make sure webpack loader always goes for dist when debug is off
if not DEBUG:
    WEBPACK_LOADER.update({
        'DEFAULT':{
            'BUNDLE_DIR_NAME': 'dist/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json')
        }
    })
