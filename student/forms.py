from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    ''' Form for creating student profile information. '''
    home_address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'home address'})
        )
    program = forms.CharField(
        widget=forms.TextInput()
    )
    department = forms.CharField(
        widget=forms.TextInput()
    )
    option = forms.CharField(
        widget=forms.TextInput()
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
    class Meta:
        model = Student
        exclude = ('user', 'is_done')