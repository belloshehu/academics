# Generated by Django 3.1.2 on 2020-10-23 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0004_lecturer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='phone_number',
        ),
    ]
