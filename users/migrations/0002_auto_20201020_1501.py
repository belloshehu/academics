# Generated by Django 3.1.2 on 2020-10-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]