# Generated by Django 5.2 on 2025-04-24 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appwebsite', '0003_alter_service_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='ServiceInfo',
        ),
    ]
