# Generated by Django 2.1.2 on 2018-10-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20181029_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='profile',
            new_name='profiles',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]