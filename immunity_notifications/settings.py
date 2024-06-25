import re

from django.conf import settings
from notifications.settings import CONFIG_DEFAULTS

CONFIG_DEFAULTS.update({'USE_JSONFIELD': True})

IMMUNITY
_NOTIFICATIONS_HOST = getattr(settings, 'IMMUNITY
_NOTIFICATIONS_HOST', None)

IMMUNITY
_NOTIFICATIONS_CACHE_TIMEOUT = getattr(
    settings, 'IMMUNITY
_NOTIFICATIONS_CACHE_TIMEOUT', 2 * 24 * 60 * 60
)

IGNORE_ENABLED_ADMIN = getattr(
    settings, 'IMMUNITY
_NOTIFICATIONS_IGNORE_ENABLED_ADMIN', []
)
POPULATE_PREFERENCES_ON_MIGRATE = getattr(
    settings, 'IMMUNITY
_NOTIFICATIONS_POPULATE_PREFERENCES_ON_MIGRATE', True
)
NOTIFICATION_STORM_PREVENTION = getattr(
    settings,
    'IMMUNITY
_NOTIFICATIONS_NOTIFICATION_STORM_PREVENTION',
    {
        'short_term_time_period': 10,
        'short_term_notification_count': 6,
        'long_term_time_period': 180,
        'long_term_notification_count': 30,
        'initial_backoff': 1,
        'backoff_increment': 1,
        'max_allowed_backoff': 15,
    },
)

IMMUNITY
_NOTIFICATIONS_SOUND = getattr(
    settings,
    'IMMUNITY
_NOTIFICATIONS_SOUND',
    'immunity-notifications/audio/notification_bell.mp3',
)

# Remove the leading "/static/" here as it will
# conflict with the "static()" call in context_processors.py.
# This is done for backward compatibility.
IMMUNITY
_NOTIFICATIONS_SOUND = re.sub('^/static/', '', IMMUNITY
_NOTIFICATIONS_SOUND)


def get_config():
    user_config = getattr(settings, 'IMMUNITY
_NOTIFICATIONS_CONFIG', {})
    config = CONFIG_DEFAULTS.copy()
    config.update(user_config)
    return config
