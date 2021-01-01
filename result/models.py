from django.db import models
from level.models import Level
from course.models import Course
from student.models import Student
from department.models import Department
from examinations.models import Examination


class Result(models.Model):
    ''' Model to represent student's academic result.'''
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    level       = models.ForeignKey(Level, on_delete=models.CASCADE)
    department  = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    student     = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade_point = models.DecimalField(
        default=0.00,
        null=True, 
        max_digits=3
    )
    grade       = models.CharField(max_length=2, null=True)
    remark      = models.CharField(max_length=15, null=True)
    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'''
            {self.course.title},
            {self.examination.semester}, 
            {self.examination.session}
        '''