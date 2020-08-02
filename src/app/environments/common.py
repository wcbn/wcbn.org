"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# dot-delimited path of settings file to use e.g. app.environments.production
DJANGO_SETTINGS_MODULE = os.environ.get("DJANGO_SETTINGS_MODULE")


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, os.pardir)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# comma delimited e.g. .example.com,www.another.com
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.sites',
    'wcbn_auth.apps.WCBNAuthConfig',
    'wcbn_core',
    'wcbn_cms.apps.WCBNCMSConfig',
    'readback',
    'ionicons',
    'trix',
    'captcha',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'guardian',
    'storages',
    'widget_tweaks',
    'django_filters',
    'phonenumber_field'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.TurbolinksMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
]

GUARDIAN_RENDER_404 = True
GUARDIAN_TEMPLATE_404 = '404.html'


LOGIN_URL = 'wcbn_auth:login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'wcbn_auth.User'


ROOT_URLCONF = 'app.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.global_config'
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

# Uploaded files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'collectedmedia')

# static assets that aren’t tied to a particular app
STATICFILES_DIRS = [
    os.path.join(SRC_DIR, "static"),
]

# Email
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = '"WCBN" <noreply@wcbn.org>'

# Phone
PHONENUMBER_DEFAULT_REGION = 'US'

DATE_INPUT_FORMATS = [
    '%m-%d-%Y', '%m-%d-%y',             # '10-25-2006', '10-25-06',
    '%m/%d/%Y', '%m/%d/%y',             # '10/25/2006', '10/25/06',
    '%m.%d.%Y', '%m.%d.%y',             # '10.25.2006', '10.25.06',
    '%m %d %Y', '%m %d %y',             # '10 25 2006', '10 25 06',
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
    '%Y-%m-%d'                          # '2006-10-25' <-- Django's annoying default :)
]

SITE_ID = 1  # used by flatpages and sites

# WCBN config
READBACK_URL = "https://app.wcbn.org"
STUDIO_LINE = "(734) 763-3500"

SOCIAL_ICONS = {
    "logo-twitter": "https://twitter.com/wcbn_fm",
    "logo-instagram": "https://instagram.com/wcbn_fm",
    # "logo-facebook": "#", #NOTE facebook is evil
    "logo-youtube": "https://www.youtube.com/channel/UCGvolMa6x_1Xc6qet5uMGRQ",
    "logo-soundcloud": "https://soundcloud.com/wcbn",
    "logo-reddit": "https://www.reddit.com/r/wcbn/",
    "logo-github": "https://github.com/wcbn"
}


RESOURCE_LINKS = {
    "WCBN Sports": "http://www.wcbnsports.org/",
    "Weekly Archive": "http://beanball.wcbn.org/listen/index.html",
    "Maize Pages": "https://maizepages.umich.edu/organization/wcbn",
    "Official Forum": SOCIAL_ICONS["logo-reddit"],
    "Community Fan Club": "https://www.facebook.com/groups/5530431845/",
    'Readback Database': READBACK_URL,
    'Give to WCBN': "https://leadersandbest.umich.edu/find/#!/give/basket/fund/361991"
}

NAV_TABS = {
    'About': 'wcbn_cms:about',
    'Contact': 'wcbn_cms:contact',
    'Events': 'wcbn_cms:events',
    'Concerts': 'wcbn_cms:concerts',
    'Schedule': 'readback:schedule',
    'Playlist': 'readback:playlist',
}

USER_NAV_TABS = {
    # 'Log in': 'wcbn_auth:login',
    # 'Sign up': 'wcbn_auth:create_user'
}

IOS_URL = 'https://apps.apple.com/us/app/wcbn-fm-ann-arbor/id600658964?mt=8'
ANDROID_URL = 'https://play.google.com/store/apps/details?id=org.wcbn'
