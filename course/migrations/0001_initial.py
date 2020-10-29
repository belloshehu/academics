# Generated by Django 3.1.2 on 2020-10-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(max_length=20, null=True)),
                ('credit_unit', models.IntegerField(default=0, null=True)),
                ('deparment', models.CharField(choices=[('EED', 'Electrical and Electronics Engineering'), ('MED', 'Mechanical Engineering Department'), ('ISET', 'Industrial Safety and Environmental Technology'), ('GS', 'General Studies'), ('PMBS', 'Petroleum Marketting and Bussiness Studies'), ('WEOT', 'Welding Engineering and Offshore Technology'), ('PNGPD', 'Petroleum and Natural Gas Processing'), ('PEG', 'Petroleum and Geo-sciences')], max_length=50, null=True)),
                ('option', models.CharField(choices=[('p&m', 'Power and Machine'), ('e&t', 'Electronics and Telecommunications'), ('i&c', 'Instrumentation and Control'), ('pp', 'Power Plant'), ('m', 'Manufacturing'), ('mre', 'Mineral Resources')], max_length=50, null=True)),
                ('semester', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third')], max_length=20, null=True)),
                ('level', models.CharField(choices=[('1', 'First year'), ('2', 'Second year'), ('3', 'Third year'), ('4', 'Fourth year'), ('5', 'Fifth year')], max_length=15, null=True)),
            ],
        ),
    ]