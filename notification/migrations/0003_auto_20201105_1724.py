# Generated by Django 3.1.2 on 2020-11-05 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0002_auto_20201027_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('abbreviated_name', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiverCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('abbreviated_name', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('message', models.TextField(max_length=200, null=True)),
                ('date_time_sent', models.DateTimeField(auto_now_add=True)),
                ('expired', models.BooleanField(default=False)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.notificationdegree')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('target_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_individualnotification_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='notification',
            name='degree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.notificationdegree'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.receivercategory'),
        ),
    ]
