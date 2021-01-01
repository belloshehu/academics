from django.db import models
from django.urls import reverse

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
