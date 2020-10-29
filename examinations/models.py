from django.db import models
from program.models import Semester, Session
from program.models import Program, ProgramType


class Examination(models.Model):
    ''' Model to represent Examinations taken by students.'''
    
    SEMESTERS = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third')
    )
    '''
    LEVELS = (
        ('1', 'First year'),
        ('2', 'Second year'),
        ('3', 'Third year'),
        ('4', 'Fourth year'),
        ('5', 'Fifth year')
    )
    PROGRAMS = (
            ('ND', 'National Diploma'),
            ('HND', 'Higher National Diploma'),
            ('GW', 'General Welding')
    )
    PROGRAM_TYPES = (
        ('1', 'Full-Time'),
        ('2', 'Part-Time')
    )
    '''
    SESSIONS = (
        ('1', '2020/2021'),
        ('2', '2021/2022'),
        ('3', '2022/2023')
    )
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    program_type = models.ForeignKey(
        ProgramType,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'{self.semester}, {self.session}'