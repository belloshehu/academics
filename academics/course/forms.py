from django import forms
from .models import Course, LecturerCourseAssignment


YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)
class CourseForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Course title e.g. Advance Algebra'}
            )
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

class LecturerCourseAssignmentForm(forms.ModelForm):
    ''' Form for assigning course to lecturers. '''
    is_joined = forms.BooleanField(
        label='to be tought by many?',
        widget=forms.Select(choices=YES_OR_NO,),
        initial=False,
        required=False

    )
    class Meta:
        model = LecturerCourseAssignment
        fields = (
            'course',
            'lecturer',
            'is_joined',
        )

    def set_course(self, course):
        self.Meta.fields.course = course
