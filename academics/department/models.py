from django.db import models
from django.urls import reverse

class Department(models.Model):
    TYPE = (
        ('1', 'academic'),
        ('2', 'non-academic')
    )
    NAME = (
        ('EED', 'Electrical and Electronics Engineering'),
        ('MED', 'Mechanical Engineering Department'),
        ('ISET', 'Industrial Safety and Environmental Technology'),
        ('GS', 'General Studies'),
        ('PMBS', 'Petroleum Marketting and Bussiness Studies'),
        ('WEOT', 'Welding Engineering and Offshore Technology'),
        ('PNGPD', 'Petroleum and Natural Gas Processing'),
        ('PEG', 'Petroleum and Geo-sciences'),
    )
    name = models.CharField(max_length=100, null=True)
    abbreviated_name = models.CharField(max_length=10, null=True)
    logo = models.FileField(upload_to='images/department', null=True)
    office = models.CharField(max_length=100, null=True)
    activity_type = models.CharField(choices=TYPE, max_length=20, default='academic')
    phone_number = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department:detail', kwargs={'pk':self.id})