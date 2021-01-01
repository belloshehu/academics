from django.db import models
from users.models import User
from django.urls import reverse

class NotificationDegree(models.Model):
    ''' Model to represent the importance level of notification.'''
    title = models.CharField(max_length=20, null=True)
    abbreviated_name = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f'{self.title}'


class ReceiverCategory(models.Model):
    ''' Model to represent category of notification receivers.'''
    title = models.CharField(max_length=20, null=True)
    abbreviated_name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.title}'


class Notification(models.Model):
    ''' Model to instantiate notifications to users.'''
    title = models.CharField(max_length=50, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=200, null=True)
    date_time_sent = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
    target_receiver = models.ForeignKey(
        ReceiverCategory,
        on_delete=models.CASCADE
    )
    degree = models.ForeignKey(
        NotificationDegree,
        on_delete=models.CASCADE
     )

    def __str__(self):
        return f'{self.title} to {self.get_target_receiver_display}'

    def get_absolute_url(self):
        return reverse('notification:notification-detail', kwargs={'pk':self.id})


class IndividualNotification(models.Model):
    '''Model to represent notifications sent to individual. '''
    title = models.CharField(max_length=50, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=200, null=True)
    date_time_sent = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
    target_receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related'
    )
    degree = models.ForeignKey(
        NotificationDegree,
        on_delete=models.CASCADE
     )

    def __str__(self):
        return f'{self.title} to {self.target_receiver.last_name}'

    def get_absolute_url(self):
        return reverse(
            'notification:individual-notification-detail',
            kwargs={'pk':self.id}
        )
