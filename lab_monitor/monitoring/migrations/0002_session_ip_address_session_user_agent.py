# Generated by Django 5.0.6 on 2024-07-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='user_agent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
