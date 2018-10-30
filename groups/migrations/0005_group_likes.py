# Generated by Django 2.1.2 on 2018-10-29 16:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0004_auto_20181029_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='_group_likes_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
