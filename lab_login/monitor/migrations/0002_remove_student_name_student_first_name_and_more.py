# Generated by Django 5.0.6 on 2024-07-21 14:09

import monitor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, validators=[monitor.models.validate_roll_no]),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]
