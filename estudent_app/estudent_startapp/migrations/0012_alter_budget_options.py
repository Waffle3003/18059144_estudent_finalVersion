# Generated by Django 3.2.9 on 2022-02-15 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudent_startapp', '0011_budget_edit_date_budget'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budget',
            options={'get_latest_by': ['user']},
        ),
    ]
