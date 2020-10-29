from django.db import models
from users.models import User
from course.models import Course
from student.models import Student
from lecturer.models import Lecturer

"""

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
    status = models.CharField(choices=COURSE_STATUS, max_length=20, null=True, default='1') 

    def __str__(self):
        return f'{self.course.title} registered by {self.student.user.username}'


class LecturerCourseAssignment(models.Model):
    ''' Model to assign a course to lecturers.'''
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_time_assigned = models.DateTimeField(auto_now_add=True)
    is_joined = models.BooleanField(default=False) # whether is assign to many lecturers
    
    def __str__(self):
        return f'{self.course.title} assigned to {self.lecturer.user.username}'
        """