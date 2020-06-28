try:
    from .common import *
except ImportError:
    print("ERROR: Unable to read shared settings")
    exit(1)

import dj_database_url

# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

DEBUG = False

# Database
DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') 
AWS_STORAGE_BUCKET_NAME = 'wcbn-org'
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = 's3v4'

# REQUIRED by captcha pkg
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
