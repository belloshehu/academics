# Generated by Django 3.1.2 on 2020-10-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]