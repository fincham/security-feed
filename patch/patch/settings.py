"""
Django settings for patch project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8xgmur-gapivo71bt5*gi7sm=mnf5x9emt4f7oy9q7o=uyz2fn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap3',
    'catalyst_bootstrap',
    'hosts',
    'advisories',
    'reporting',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'patch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'patch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'patch',
        'USER': 'patch',
        'PASSWORD': 'patch',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'advisories_cache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-nz.UTF-8'

TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


ADVISORY_SOURCES = (
    ('ubuntu', 'Ubuntu'),
    ('debian', 'Debian'),
)

# For advisories that have been triaged by a human
ADVISORY_SEVERITIES = (
    (0, 'Undecided'),
    (1, 'Low'),
    (2, 'Standard'),
    (3, 'High'),
    (4, 'Critical'),
)

ADVISORY_SEVERITY_CLASSES = (
    (0, ''),
    (1, 'text-muted'),
    (2, 'text-info'),
    (3, 'text-warning'),
    (4, 'text-danger'),
)

# Current stable releases
RELEASES = (
    ('squeeze', 'Debian Squeeze 6.0'),
    ('wheezy', 'Debian Wheezy 7.0'),
    ('jessie', 'Debian Jessie 8.0'),
    ('precise', 'Ubuntu Precise LTS 12.04'),
    ('trusty', 'Ubuntu Trusty LTS 14.04',)
)

# Data source plugins
DATA_SOURCES = (
    ('hostinfo', 'hostinfo'),
)

SOURCE_ADVISORY_DETAIL_URLS = {
    ('ubuntu', 'http://www.ubuntu.com/usn/%s/'),
    ('debian', 'https://security-tracker.debian.org/tracker/%s'),
}

SOURCE_PACKAGE_DETAIL_URLS = {
    ('ubuntu', 'http://packages.ubuntu.com/%s/%s'),
    ('debian', 'https://packages.debian.org/%s/%s'),
}

APTGET_COMMAND_STUB = 'sudo apt-get --only-upgrade install'

ADVISORYCACHE_EMPTYRESULT = 'empty'
ADVISORYCACHE_KEYS = {'affected_hosts': 'affected_hosts_%s',
    'resolved_hosts': 'resolved_hosts_%s',
    'unresolved_hosts': 'unresolved_hosts_%s'}
