# Generated by Django 3.0.4 on 2020-11-10 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_event_time_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time_zone',
        ),
    ]