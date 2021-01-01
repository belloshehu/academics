from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    ''' Form for creating student profile information. '''
    STUDENT_POSITION = (
        (True, 'Yes'),
        (False, 'No'),
        (None, '---Select Yes or No---')
    )
    home_address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'home address'})
        )
    matriculation_no = forms.CharField(
        widget=forms.TextInput()
    )
    year_of_admission = forms.CharField(
        widget=forms.TextInput(attrs={'type':'date'})
    )
    year_of_graduation = forms.CharField(
        widget=forms.TextInput(attrs={'type':'date'})
    )
    is_course_ref = forms.BooleanField(
        label='Are you course representative?',
        widget=forms.Select(choices=STUDENT_POSITION),
        initial=None
    )
    class Meta:
        model = Student
        exclude = ('user','is_done',)