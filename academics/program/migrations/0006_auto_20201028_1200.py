# Generated by Django 3.1.2 on 2020-10-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_auto_20201028_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='end_month',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='start_month',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_year',
            field=models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_year',
            field=models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True),
        ),
    ]