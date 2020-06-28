try:
    from .common import *
except ImportError:
    print("ERROR: Unable to read shared settings")
    exit(1)

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS += [ 
    'debug_toolbar',
    'django_extensions'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
    "INSERT_BEFORE": '</head>'
}

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
