# Generated by Django 3.1.2 on 2020-11-04 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0006_department_logo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('option', '0003_option_abbreviated_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('photo', models.FileField(default=None, null=True, upload_to='images/lecturers')),
                ('is_serving', models.BooleanField(default=False, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
