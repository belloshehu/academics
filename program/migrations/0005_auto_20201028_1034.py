# Generated by Django 3.1.2 on 2020-10-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20201028_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_year',
            field=models.IntegerField(choices=[(2020, 2020)], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_year',
            field=models.IntegerField(choices=[(2020, 2020)], max_length=5, null=True, verbose_name='start year'),
        ),
    ]
