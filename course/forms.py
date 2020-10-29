from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Course title e.g. Advance Algebra'}
            )
    )
    option = forms.CharField(
        widget=forms.Select(choices=Course.OPTIONS), 
        initial='0',
    )
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Course code e.g. MTH321'}
            )
    )
    class Meta:
        model = Course
        fields = '__all__'

    def clean_credit_unit(self):
        credit_unit = self.cleaned_data.get('credit_unit')
        if credit_unit > 0:
            return credit_unit
        else:
            return forms.ValidationError('Credit unit must be greater than 0') 
    
    def clean_option(self):
        option = self.cleaned_data.get('option')
        if option != '0':
            return option
        else:
            return forms.ValidationError('Select a valid option')
