# Generated by Django 3.1.2 on 2020-10-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20201021_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.TextField(choices=[('EED', 'Electrical and Electronics Engineering'), ('MED', 'Mechanical Engineering Department'), ('ISET', 'Industrial Safety and Environmental Technology'), ('GS', 'General Studies'), ('PMBS', 'Petroleum Marketting and Bussiness Studies'), ('WEOT', 'Welding Engineering and Offshore Technology'), ('PNGPD', 'Petroleum and Natural Gas Processing'), ('PEG', 'Petroleum and Geo-sciences')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='option',
            field=models.TextField(choices=[('p&m', 'Power and Machine'), ('e&t', 'Electronics and Telecommunications'), ('i&c', 'Instrumentation and Control'), ('pp', 'Power Plant'), ('m', 'Manufacturing'), ('mre', 'Mineral Resources')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.TextField(choices=[('ND', 'National Diploma'), ('HND', 'Higher National Diploma'), ('GW', 'General Welding')], null=True),
        ),
    ]