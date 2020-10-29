from django.db import models
from users.models import User
from django.urls import reverse


class Notification(models.Model):
    ''' Model to instantiate notifications to users.'''
    TARGET = (
        ('1', 'All'),
        ('2', 'Student only'),
        ('3', 'Staffs only'),
        ('4', 'Lecturers only'),
        ('5', 'Lecturers and Teachers only'),
        ('6', 'HODs only')
    )
    DEGREE = (
        ('1', 'Warning'),
        ('2', 'Info'),
        ('3', 'Danger'),
        ('4', 'Hint/Advice')
    )
    title = models.CharField(max_length=50, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=200, null=True)
    date_time_sent = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
    target_receiver = models.CharField(choices=TARGET, max_length=30, null=True)
    degree = models.CharField(choices=DEGREE, max_length=20, default='2')

    def __str__(self):
        return f'{self.title} to {self.get_target_receiver.display}'

    def get_absolute_url(self):
        object_id = self.id
        return reverse('notification:notification-detail', kwargs={'pk':object_id})
