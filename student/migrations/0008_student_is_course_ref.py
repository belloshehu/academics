# Generated by Django 3.1.2 on 2020-10-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_student_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_course_ref',
            field=models.BooleanField(default=False, null=True),
        ),
    ]