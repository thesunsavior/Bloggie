# Generated by Django 3.2.13 on 2022-06-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_fb_user_gg_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='fb_user',
            name='info',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gg_user',
            name='info',
            field=models.BooleanField(default=False),
        ),
    ]
