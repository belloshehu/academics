from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(blank=True, max_length=50, null=True)
    date_of_birth = models.DateField(auto_now_add=True)
    is_student = models.BooleanField(default=False, null=True)
    is_lecturer = models.BooleanField(default=False, blank=True)
    is_hod = models.BooleanField(default=False, blank=True)
    phone_number = models.CharField(max_length=11, null=True)
    approved = models.BooleanField(default=False, null=True)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name}'