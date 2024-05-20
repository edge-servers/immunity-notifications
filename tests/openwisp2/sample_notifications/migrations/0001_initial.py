# Generated by Django 3.0.5 on 2020-04-14 18:32

import uuid

import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import swapper
from django.conf import settings
from django.db import migrations, models

from immunity_notifications.types import NOTIFICATION_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('immunity_users', '0009_create_organization_owners'),
        swapper.dependency('immunity_users', 'Organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                (
                    'level',
                    models.CharField(
                        choices=[
                            ('success', 'success'),
                            ('info', 'info'),
                            ('warning', 'warning'),
                            ('error', 'error'),
                        ],
                        default='info',
                        max_length=20,
                        verbose_name='level',
                    ),
                ),
                (
                    'unread',
                    models.BooleanField(
                        db_index=True, default=True, verbose_name='unread'
                    ),
                ),
                (
                    'actor_object_id',
                    models.CharField(max_length=255, verbose_name='actor object id'),
                ),
                ('verb', models.CharField(max_length=255, verbose_name='verb')),
                (
                    'description',
                    models.TextField(blank=True, null=True, verbose_name='description'),
                ),
                (
                    'target_object_id',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name='target object id',
                    ),
                ),
                (
                    'action_object_object_id',
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name='action object object id',
                    ),
                ),
                (
                    'timestamp',
                    models.DateTimeField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        verbose_name='timestamp',
                    ),
                ),
                (
                    'public',
                    models.BooleanField(
                        db_index=True, default=True, verbose_name='public'
                    ),
                ),
                (
                    'deleted',
                    models.BooleanField(
                        db_index=True, default=False, verbose_name='deleted'
                    ),
                ),
                (
                    'emailed',
                    models.BooleanField(
                        db_index=True, default=False, verbose_name='emailed'
                    ),
                ),
                (
                    'data',
                    jsonfield.fields.JSONField(
                        blank=True, null=True, verbose_name='data'
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'action_object_content_type',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='notify_action_object',
                        to='contenttypes.ContentType',
                        verbose_name='action object content type',
                    ),
                ),
                (
                    'actor_content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='notify_actor',
                        to='contenttypes.ContentType',
                        verbose_name='actor content type',
                    ),
                ),
                (
                    'recipient',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='notifications',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='recipient',
                    ),
                ),
                (
                    'target_content_type',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='notify_target',
                        to='contenttypes.ContentType',
                        verbose_name='target content type',
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=NOTIFICATION_CHOICES,
                        max_length=30,
                        null=True,
                    ),
                ),
                ('details', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'ordering': ('-timestamp',),
                'abstract': False,
                'index_together': {('recipient', 'unread')},
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=NOTIFICATION_CHOICES,
                        max_length=30,
                        null=True,
                        verbose_name='Notification Type',
                    ),
                ),
                (
                    'web',
                    models.BooleanField(
                        null=True,
                        blank=True,
                        help_text=(
                            'Note: Non-superadmin users receive notifications only '
                            'for organizations of which they are member of.'
                        ),
                        verbose_name='web notifications',
                    ),
                ),
                (
                    'email',
                    models.BooleanField(
                        null=True,
                        blank=True,
                        help_text=(
                            'Note: Non-superadmin users receive notifications only '
                            'for organizations of which they are member of.'
                        ),
                        verbose_name='email notifications',
                    ),
                ),
                ('details', models.CharField(blank=True, max_length=64, null=True)),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('immunity_users', 'Organization'),
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'deleted',
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name='Delete'
                    ),
                ),
            ],
            options={
                'verbose_name': 'user notification settings',
                'verbose_name_plural': 'user notification settings',
                'ordering': ['organization', 'type'],
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='notificationsetting',
            constraint=models.UniqueConstraint(
                fields=('organization', 'type', 'user'),
                name='unique_notification_setting',
            ),
        ),
        migrations.AddIndex(
            model_name='notificationsetting',
            index=models.Index(
                fields=['type', 'organization'], name='sample_noti_type_b2cb70_idx'
            ),
        ),
        migrations.CreateModel(
            name='IgnoreObjectNotification',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('object_id', models.CharField(max_length=255)),
                ('valid_till', models.DateTimeField(null=True)),
                ('details', models.CharField(blank=True, max_length=64, null=True)),
                (
                    'object_content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contenttypes.ContentType',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={'abstract': False, 'ordering': ['valid_till']},
        ),
    ]
