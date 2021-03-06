# Generated by Django 3.1.2 on 2020-10-20 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(choices=[('p&m', 'Power and Machine'), ('e&t', 'Electronics and Telecommunications'), ('i&c', 'Instrumentation and Control'), ('pp', 'Power Plant'), ('m', 'Manufacturing'), ('mre', 'Mineral Resources')])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]
