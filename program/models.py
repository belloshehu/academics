from django.db import models
from .model_extension import generate_years_list

class ProgramType(models.Model):
    ''' Model to represent type of programs. '''
    name = models.CharField(max_length=30, null=True)

    def get_absolute_url(self):
        return reverse(
            'program_type:program_type-detail',
            kwargs={'pk', self.id}
    )
    def __str__(self):
        return self.name


class Program(models.Model):
    ''' Represent programs in Schools. '''
    name = models.CharField(max_length=50, null=True)
    duration = models.IntegerField(default=0)
    cost = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    program_type = models.ForeignKey(
        ProgramType,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f'{self.name}, {self.duration} months'


class Session(models.Model):
    ''' Model to represent academic session. '''
    YEAR_CHOICES = generate_years_list()
    name = models.CharField(max_length=10, null=True)
    start_year = models.IntegerField(choices=YEAR_CHOICES, null=True)
    end_year = models.IntegerField(choices=YEAR_CHOICES, null=True)

    def __str__(self):
        return f'from {self.start_year}, to {self.end_year}'

    def get_full_session(self):
        ''' Returns session in started_year/ended_year format.'''
        return f'''
                {self.start_year.year}/{self.end_year.year}
            '''

class Semester(models.Model):
    MONTH_CHOICES = (
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    )
    ''' Model to represent semester in academic session.'''
    name = models.CharField(max_length=30)
    duration = models.IntegerField(null=True)
    start_month = models.CharField(choices=MONTH_CHOICES, max_length=10, null=True)
    end_month = models.CharField(choices=MONTH_CHOICES, max_length=10, null=True)

    def __str__(self):
        return self.name

    def get_duration(self):
        ''' Returns duration of semester in months. '''
        return abs(int(self.end_month) - int(self.start_month))

    def save(self, *args, **kwargs):
        if self.duration != int(self.end_month) - int(self.start_month):
            return
        else:
            super().save(*args, **kwargs)