# Generated by Django 4.2.1 on 2024-07-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options_alter_women_is_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
