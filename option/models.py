from django.db import models
from department.models import Department


class Option(models.Model):
    ''' Represent a major in field of study
        such as electronics in Electrical and Electronic
        Engineering.
    '''
    '''
    OPTIONS = (
        ('p&m', 'Power and Machine'),
        ('e&t', 'Electronics and Telecommunications'),
        ('i&c', 'Instrumentation and Control'),
        ('pp', 'Power Plant'),
        ('m', 'Manufacturing'),
        ('mre', 'Mineral Resources')
    )
    '''
    name = models.CharField(max_length=60, null=True)
    abbreviated_name = models.CharField(max_length=15, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} in {self.department.name}'
