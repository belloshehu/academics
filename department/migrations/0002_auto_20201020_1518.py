# Generated by Django 3.1.2 on 2020-10-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='activity_type',
            field=models.TextField(choices=[('1', 'academic'), ('2', 'non-academic')], default='academic'),
        ),
    ]
