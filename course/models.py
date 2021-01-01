from django.db import models
from django.urls import reverse
from users.models import User
from level.models import Level
from option.models import Option
from student.models import Student
from program.models import (
    Semester,
    ProgramType,
    Program
)
from lecturer.models  import Lecturer
from department.models import Department

class Course(models.Model):
    ''' Course in academic institution. '''
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


class StudentCourseRegistration(models.Model):
    ''' Model to assign courses to students. '''
    COURSE_STATUS = (
        ('1', 'Fresh Course'),
        ('2', 'Carry over'),
        ('3', 'Spill over')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_time_registered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=COURSE_STATUS,
        max_length=20, null=True,
        default='1'
    )

    def __str__(self):
        return f'{self.course.title} registered by {self.student.user.username}'


class LecturerCourseAssignment(models.Model):
    ''' Model to assign a course to lecturers.'''
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_time_assigned = models.DateTimeField(auto_now_add=True)
    # whether is assign to many lecturers
    is_joined = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f'{self.course.title} assigned to {self.lecturer.user.username}'


class CourseDistribution(models.Model):
    ''' Model to distribute courses to different department and options.'''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f'''
            {self.course.code} to
            {self.department.abbreviated_name}|
            {self.option.abbreviated_name}
        '''