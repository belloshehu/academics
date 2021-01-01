from django.db import models
from django.urls import reverse

class Level(models.Model):
    ''' Model to represent class level of student. '''
    name = models.CharField(max_length=50, null=True)
    abbreviated_name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('level:level-detail', kwargs={'pk':self.id})