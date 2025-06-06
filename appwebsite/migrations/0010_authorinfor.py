# Generated by Django 5.2 on 2025-05-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwebsite', '0009_bloginfo_context'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('joined_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
