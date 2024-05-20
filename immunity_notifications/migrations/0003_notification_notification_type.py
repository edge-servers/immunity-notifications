from django.db import migrations, models

from immunity_notifications.types import NOTIFICATION_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('immunity_notifications', '0002_default_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(
                choices=NOTIFICATION_CHOICES,
                max_length=30,
                null=True,
            ),
        ),
    ]
