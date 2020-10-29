from django.db import models
from users.models import User
from django.urls import reverse
from option.models import Option
from department.models import Department
from course.models  import Course


class Lecturer(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    office = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    photo  = models.FileField(upload_to='media/images', null=True, default=None)
    is_hod = models.BooleanField(default=False, null=True)
    is_serving = models.BooleanField(default=False)
    #course = models.ManyToManyField(Course, through='LecturerCourseAssignment')


    def __str__(self):
        return f'{self.user.get_full_name} | {self.department}'

    def get_absolute_url(self):
        return reverse('lecturer:lecturer-detail', kwargs={'pk':self.id})
