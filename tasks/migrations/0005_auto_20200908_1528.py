# Generated by Django 2.2.16 on 2020-09-08 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200908_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
