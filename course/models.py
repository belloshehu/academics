from django.db import models
from django.urls import reverse
from users.models import User
from level.models import Level
from option.models import Option
from program.models import Semester
from department.models import Department

class Course(models.Model):
    ''' Course in academic institution. '''
    SEMESTERS = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third')
    )
    LEVELS = (
        ('1', 'First year'),
        ('2', 'Second year'),
        ('3', 'Third year'),
        ('4', 'Fourth year'),
        ('5', 'Fifth year')
    )
    OPTIONS = (
        ('p&m', 'Power and Machine'),
        ('e&t', 'Electronics and Telecommunications'),
        ('i&c', 'Instrumentation and Control'),
        ('pp', 'Power Plant'),
        ('m', 'Manufacturing'),
        ('mre', 'Mineral Resources'),
        ('0', '--- Select an option ---')
    )
    DEPARTMENTS = (
        ('EED', 'Electrical and Electronics Engineering'),
        ('MED', 'Mechanical Engineering Department'),
        ('ISET', 'Industrial Safety and Environmental Technology'),
        ('GS', 'General Studies'),
        ('PMBS', 'Petroleum Marketting and Bussiness Studies'),
        ('WEOT', 'Welding Engineering and Offshore Technology'),
        ('PNGPD', 'Petroleum and Natural Gas Processing'),
        ('PEG', 'Petroleum and Geo-sciences'),
    )
    title = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=20, null=True)
    credit_unit = models.IntegerField(default=0, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
     
    def __str__(self):
        return f'{self.title} - {self.department}'

    def get_absolute_url(self):
        return reverse('course:course-detail', kwargs={'pk': self.id})
