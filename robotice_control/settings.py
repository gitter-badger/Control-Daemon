# -*- coding: utf-8 -*-
{%- from "robotice_control/map.jinja" import server with context %}

from os.path import join, dirname, abspath, normpath

from config import DEFAULT_DATABASE, DEFAULT_CACHE, DEFAULT_EMAIL, \
                   RAVEN_CONFIG, DEFAULT_BROKER as BROKER_URL

ALLOWED_HOSTS = ['*']

CACHES = {
    'default': DEFAULT_CACHE
}

DATABASES = {
    'default': DEFAULT_DATABASE
}

EMAIL_HOST = DEFAULT_EMAIL['HOST']
EMAIL_HOST_USER = DEFAULT_EMAIL['USER']
EMAIL_HOST_PASSWORD = DEFAULT_EMAIL['PASSWORD']
EMAIL_USE_TLS = DEFAULT_EMAIL['SECURITY']

USE_TZ = True

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'mail@newt.cz'),
    ('Majklk', 'mail@majklk.cz'),
)

MANAGERS = ADMINS

SITE_ID = 1

SITE_NAME = 'robotice_control'

TIME_ZONE = 'Europe/Prague'
{#
TIME_ZONE = '{{ pillar.system.timezone }}'
#}

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('cs', 'CS'),
    ('en', 'EN'),
)

USE_I18N = True

MEDIA_ROOT = '/srv/robotice_control/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/srv/robotice_control/static/'
STATIC_URL = '/static/'

SECRET_KEY = '{{ server.secret_key }}'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'robotice_control.urls'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django',
    'django_extensions',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'south',
    'rest_framework',
    'robotice_control',
    {% if server.logging is defined %}
    'raven.contrib.django.raven_compat',
    {% endif %}
)

STATICFILES_FINDERS =(
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/admin/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'openstack_auth.backend.KeystoneBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

{%- if server.metric is defined %}

{%- if server.metric.get("in", {"engine": ""}).engine == 'graphite' %}
GRAPHITE_HOST = "{{ server.metric.in.host }}"
GRAPHITE_PORT = "{{ server.metric.in.port }}"
GRAPHITE_ENDPOINT = 'http://%s:%s' % (GRAPHITE_HOST, GRAPHITE_PORT)
{%- endif %}

{%- if server.metric.get("out", {"engine": ""}).engine == 'statsd' %}
STATSD_HOST = "{{ server.metric.out.host }}"
STATSD_PORT = "{{ server.metric.out.get('port', 8125) }}"
STATSD_PREFIX = "{{ server.metric.out.get('prefix', '') }}"
{%- endif %}

{%- if server.metric.get("out", {"engine": ""}).engine == 'carbon' %}
CARBON_HOST = "{{ server.metric.out.host }}"
CARBON_PORT = "{{ server.metric.out.get('port', 2003) }}"
{%- endif %}

{%- endif %}

RAVEN_CONFIG = {
{% if server.logging is defined %}
    'dsn': '{{ server.logging.dsn }}',
{% endif %}
}
{% if server.logging is defined %}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/srv/robotice_control/logs/robotice_control.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}
{% endif %}
