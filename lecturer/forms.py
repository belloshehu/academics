from django import forms
from .models import Lecturer


class LecturerForm(forms.ModelForm):
    ''' Form to create, and update lecturer instance. '''
    class Meta:
        model = Lecturer
        exclude = ('user','is_serving',)
