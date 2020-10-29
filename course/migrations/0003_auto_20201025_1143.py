# Generated by Django 3.1.2 on 2020-10-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20201024_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='option',
            field=models.CharField(choices=[('p&m', 'Power and Machine'), ('e&t', 'Electronics and Telecommunications'), ('i&c', 'Instrumentation and Control'), ('pp', 'Power Plant'), ('m', 'Manufacturing'), ('mre', 'Mineral Resources'), ('0', '--- Select an option ---')], max_length=50, null=True),
        ),
    ]
