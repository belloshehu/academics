from django.db import models
from users.models import User
from django.urls import reverse
from option.models import Option
from department.models import Department


class Lecturer(models.Model):
    ''' Model to repsent Lecturer instance. '''
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    office = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    photo  = models.FileField(upload_to='images/lecturers', null=True)
    is_serving = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.user.get_full_name} | {self.department.abbreviated_name}'

    def get_absolute_url(self):
        return reverse('lecturer:lecturer-detail', kwargs={'pk':self.id})

    def save(self, *args, **kwargs):
        if self.user.is_student or (self.user.is_staff and not self.user.is_lecturer):
            return
        else:
            super().save(*args, **kwargs)
