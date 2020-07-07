# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.template import Library
from django.utils.html import format_html
from notifications.templatetags.notifications_tags import (
    notifications_unread as base_notification_unread,
)
from openwisp_notifications.swapper import load_model

Notification = load_model('Notification')

register = Library()


def get_notifications_count(context):
    user_pk = context['user'].is_authenticated and context['user'].pk
    cache_key = Notification.COUNT_CACHE_KEY.format(user_pk)
    count = cache.get(cache_key)
    if count is None:
        count = base_notification_unread(context)
        count = '99+' if count > 99 else count
        cache.set(cache_key, count)
    return count


def unread_notifications(context):
    count = get_notifications_count(context)
    output = ''
    if count:
        output = '<span>{0}</span>'
        output = format_html(output.format(count))
    return output


def notification_widget(context):
    return format_html(
        '''
        <div class="notification-dropdown hide">
            <div class="filters">
                <span class="btn" id="mark-all-read" tabindex="1" role="button">Mark all read</span>
                <span class="btn" id="show-unread" tabindex="2" role="button">Show unread only</span>
            </div>
            <div class="notification-wrapper round-bottom-border"></div>
            <div class="no-notifications round-bottom-border hide">
                <p>No new notification.</p>
            </div>
            <div class="loader-wrapper"><div class="loader"></div></div>
        </div>
        '''
    )


register.simple_tag(takes_context=True)(unread_notifications)
register.simple_tag(takes_context=True)(notification_widget)
