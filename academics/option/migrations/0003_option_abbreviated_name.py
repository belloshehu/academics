# Generated by Django 3.1.2 on 2020-10-31 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0002_auto_20201028_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='abbreviated_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]