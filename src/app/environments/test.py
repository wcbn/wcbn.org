try:
    from .common import *
except ImportError:
    print("ERROR: Unable to read shared settings")
    exit(1)

import dj_database_url

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

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
