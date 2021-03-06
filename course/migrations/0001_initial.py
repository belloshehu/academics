# Generated by Django 3.1.2 on 2020-11-04 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '0006_auto_20201028_1200'),
        ('department', '0006_department_logo'),
        ('student', '__first__'),
        ('level', '0001_initial'),
        ('lecturer', '0001_initial'),
        ('option', '0003_option_abbreviated_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(max_length=20, null=True)),
                ('credit_unit', models.IntegerField(default=0, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='level.level')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.semester')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourseRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_registered', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', 'Fresh Course'), ('2', 'Carry over'), ('3', 'Spill over')], default='1', max_length=20, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='LecturerCourseAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_assigned', models.DateTimeField(auto_now_add=True)),
                ('is_joined', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecturer.lecturer')),
            ],
        ),
    ]
