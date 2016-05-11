from dwtest.config.settings_common import *
import os


########## DEBUG CONFIGURATION
DEBUG = False
ALLOWED_HOSTS = ['*']
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
########## END DATABASE CONFIGURATION



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

#location of your media on your disk
#MEDIA_ROOT = ''

#url wherever you store your media stuff. Nginx/Apache. 
#MEDIA_URL  = ''

if not DEBUG:
    WEBPACK_LOADER.update({
        'DEFAULT':{
            'BUNDLE_DIR_NAME': 'dist/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json')
        }
    })


