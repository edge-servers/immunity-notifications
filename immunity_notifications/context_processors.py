from django.templatetags.static import static

from immunity_notifications import settings as app_settings


def notification_api_settings(request):
    return {
        'IMMUNITY
_NOTIFICATIONS_HOST': app_settings.IMMUNITY
_NOTIFICATIONS_HOST,
        'IMMUNITY
_NOTIFICATIONS_SOUND': static(
            app_settings.IMMUNITY
_NOTIFICATIONS_SOUND
        ),
    }
