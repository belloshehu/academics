# Generated by Django 3.1.2 on 2020-10-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20201028_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='abbreviated_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]