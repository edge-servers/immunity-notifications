"""
You don't need to have this file unless you plan to modify the API views as well.
"""

from immunity_notifications.api.views import (
    IgnoreObjectNotificationListView as BaseIgnoreObjectNotificationListView,
)
from immunity_notifications.api.views import (
    IgnoreObjectNotificationView as BaseIgnoreObjectNotificationView,
)
from immunity_notifications.api.views import (
    NotificationDetailView as BaseNotificationDetailView,
)
from immunity_notifications.api.views import (
    NotificationListView as BaseNotificationListView,
)
from immunity_notifications.api.views import (
    NotificationReadAllView as BaseNotificationReadAllView,
)
from immunity_notifications.api.views import (
    NotificationSettingListView as BaseNotificationSettingListView,
)
from immunity_notifications.api.views import (
    NotificationSettingView as BaseNotificationSettingView,
)


class NotificationListView(BaseNotificationListView):
    """
    Lists user's notifications
    """

    pass


class NotificationDetailView(BaseNotificationDetailView):
    """
    Retrives details for a notification and provides endpoints
    for marking a notification read and delete it.
    """

    pass


class NotificationReadAllView(BaseNotificationReadAllView):
    """
    Marks all notifications as read
    """

    pass


class NotificationSettingView(BaseNotificationSettingView):
    """
    Retrives details for a notification setting and provides
    endpoints for updating and deleting them.
    """

    pass


class NotificationSettingListView(BaseNotificationSettingListView):
    """
    Lists user's notification settings.
    """

    pass


class IgnoreObjectNotificationView(BaseIgnoreObjectNotificationView):
    """
    Retrives details for a IgnoreNotificationObject object and
    provides endpoints for updating and deleting it.
    """

    pass


class IgnoreObjectNotificationListView(BaseIgnoreObjectNotificationListView):
    """
    Lists user's IgnoreObjectNotification objects.
    """

    pass
