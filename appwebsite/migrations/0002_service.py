# Generated by Django 5.2 on 2025-04-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('tittle', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
