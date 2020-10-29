# Generated by Django 3.1.2 on 2020-10-29 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20201028_1200'),
        ('department', '0006_department_logo'),
        ('level', '0001_initial'),
        ('option', '0002_auto_20201028_1016'),
        ('student', '0008_student_is_course_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='level.level'),
        ),
        migrations.AlterField(
            model_name='student',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option'),
        ),
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.program'),
        ),
    ]