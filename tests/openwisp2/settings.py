import os
import sys
from datetime import timedelta

TESTING = 'test' in sys.argv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

ALLOWED_HOSTS = []
INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'immunity_notifications.db'),
    }
}

SECRET_KEY = 'fn)t*+$)ugeyip6-#txyy$5wf2ervc0d2n#h)qb)y5@ly$t*@w'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_filters',
    'immunity_users',
    # notifications module
    'immunity_notifications',
    # add immunity theme
    # (must be loaded here)
    'immunity_utils.admin_theme',
    # admin
    'admin_auto_filters',
    'django.contrib.admin',
    # rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    # channels
    'channels',
    # CORS
    'corsheaders',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'immunity_utils.staticfiles.DependencyFinder',
]

AUTH_USER_MODEL = 'immunity_users.User'
SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'immunity2.urls'

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'en-gb'
USE_TZ = True
USE_I18N = False
USE_L10N = False
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
EMAIL_PORT = '1025'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'immunity_utils.loaders.DependencyLoader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'immunity_utils.admin_theme.context_processor.menu_groups',
                'immunity_utils.admin_theme.context_processor.admin_theme_settings',
                'immunity_notifications.context_processors.notification_api_settings',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost/5',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

ASGI_APPLICATION = 'immunity2.asgi.application'

if TESTING:
    CHANNEL_LAYERS = {
        'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'},
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                'hosts': ['redis://localhost/7'],
                'group_expiry': 3600,
                'capacity': 1000,
                'expiry': 30,
            },
        },
    }

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

LOGGING = {
    'version': 1,
    'filters': {'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'}},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'py.warnings': {'handlers': ['console'], 'propagate': False},
        'celery': {'handlers': ['console'], 'level': 'DEBUG'},
    },
}

if not TESTING:
    LOGGING.update({'root': {'level': 'INFO', 'handlers': ['console']}})

if not TESTING:
    CELERY_BROKER_URL = 'redis://localhost/6'
else:
    CELERY_TASK_ALWAYS_EAGER = True
    CELERY_TASK_EAGER_PROPAGATES = True
    CELERY_BROKER_URL = 'memory://'

# Workaround for stalled migrate command
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'max_retries': 10,
}

CELERY_BEAT_SCHEDULE = {
    'delete_old_notifications': {
        'task': 'immunity_notifications.tasks.delete_old_notifications',
        'schedule': timedelta(days=1),
        'args': (90,),
    },
}

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
IMMUNITY
_ADMIN_SHOW_USERLINKS_BLOCK = True
IMMUNITY
_API_DOCS = True
IMMUNITY
_USERS_AUTH_API = True
IMMUNITY
_NOTIFICATIONS_IGNORE_ENABLED_ADMIN = ['immunity_users.admin.OrganizationAdmin']
TEST_RUNNER = 'immunity_utils.tests.TimeLoggingTestRunner'

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from immunity2.local_settings import *
except ImportError:
    pass

if os.environ.get('SAMPLE_APP', False):
    INSTALLED_APPS.remove('immunity_notifications')
    EXTENDED_APPS = ['immunity_notifications']
    INSTALLED_APPS.append('immunity2.sample_notifications')
    IMMUNITY
_NOTIFICATIONS_NOTIFICATION_MODEL = 'sample_notifications.Notification'
    IMMUNITY
_NOTIFICATIONS_NOTIFICATIONSETTING_MODEL = (
        'sample_notifications.NotificationSetting'
    )
    TEMPLATES[0]['DIRS'] = [
        os.path.join(BASE_DIR, 'sample_notifications', 'templates'),
        os.path.join(
            os.path.dirname(os.path.dirname(BASE_DIR)),
            'immunity_notifications',
            'templates',
        ),
    ]
    IMMUNITY
_NOTIFICATIONS_IGNOREOBJECTNOTIFICATION_MODEL = (
        'sample_notifications.IgnoreObjectNotification'
    )
    # Celery auto detects tasks only from INSTALLED_APPS
    CELERY_IMPORTS = ('immunity_notifications.tasks',)
