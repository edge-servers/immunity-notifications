from django.contrib import admin

from immunity_notifications.base.admin import NotificationSettingAdminMixin
from immunity_notifications.swapper import load_model
from immunity_notifications.widgets import _add_object_notification_widget
from immunity_users.admin import UserAdmin
from immunity_utils.admin import AlwaysHasChangedMixin

Notification = load_model('Notification')
NotificationSetting = load_model('NotificationSetting')


class NotificationSettingInline(
    NotificationSettingAdminMixin, AlwaysHasChangedMixin, admin.TabularInline
):
    model = NotificationSetting
    extra = 0

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user == obj


UserAdmin.inlines = [NotificationSettingInline] + UserAdmin.inlines

_add_object_notification_widget()
