# Generated by Django 3.1.2 on 2020-11-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturercourseassignment',
            name='is_joined',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
