# Generated by Django 3.1.2 on 2020-10-27 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program_type', '0001_initial'),
        ('examinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='program_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program_type.programtype'),
        ),
    ]
