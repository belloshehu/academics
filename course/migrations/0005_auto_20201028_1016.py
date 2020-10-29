# Generated by Django 3.1.2 on 2020-10-28 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20201028_1016'),
        ('department', '0003_auto_20201024_1422'),
        ('option', '0002_auto_20201028_1016'),
        ('course', '0004_auto_20201028_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option'),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.semester'),
        ),
    ]