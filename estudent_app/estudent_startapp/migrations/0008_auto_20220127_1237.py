# Generated by Django 3.2.9 on 2022-01-27 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudent_startapp', '0007_auto_20220125_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='needs',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='savings',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='wants',
        ),
    ]
