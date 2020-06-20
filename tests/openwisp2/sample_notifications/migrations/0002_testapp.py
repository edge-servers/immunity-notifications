# Generated by Django 3.0.6 on 2020-06-15 20:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_users', '0007_unique_email'),
        ('sample_notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestApp',
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
                ('name', models.CharField(max_length=50)),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='openwisp_users.Organization',
                    ),
                ),
            ],
            options={'verbose_name': 'Test App', 'verbose_name_plural': 'Test App',},
        ),
    ]