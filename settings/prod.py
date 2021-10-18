import os
from settings import *  # noqa
import dj_database_url

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SECRET_KEY = os.environ['PRODUCTION_KEY']

DATABASES['default'] = dj_database_url.config(conn_max_age=600)
DATABASES['default'] = dj_database_url.config(default=os.environ['DATABASE_URL'])

DEBUG = True
MIDDLEWARE_DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
