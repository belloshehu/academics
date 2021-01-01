from django.db import models
from users.models import User
from level.models import Level
from option.models import Option
from program.models import Program
from department.models import Department
#from course_registration.models import StudentCourseRegistration


class Student(models.Model):
    ''' Model to represent Student instance. '''
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    matriculation_no = models.CharField(max_length=30, blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDERS, max_length=10)
    photo = models.FileField(upload_to='images/students', null=True)
    is_done = models.BooleanField(default=False)
    is_course_ref = models.BooleanField(default=False, null=True)
    year_of_admission = models.DateField()
    year_of_graduation = models.DateField()

    def __str__(self):
        return f'{self.user.username} @ {self.department}'
