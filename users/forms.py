from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username =forms.CharField(
        label='', widget=forms.TextInput(
        attrs={'placeholder':'Enter username', 'size':30})
    )
    password =forms.CharField(
        label='', widget=forms.PasswordInput(
        attrs={'placeholder':'Enter password', 'size':30})
    )


class StudentRegistrationForm(UserCreationForm):
    """Customer registration form."""
    username = forms.CharField(
        max_length=100, required=True, help_text='', label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )

    first_name = forms.CharField(
        max_length=100, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )
    last_name = forms.CharField(
        max_length=100, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )
    middle_name = forms.CharField(
        max_length=100, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Middle name'})
    )
    email = forms.EmailField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    phone_number = forms.CharField(
        max_length=11, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )
    password1 = forms.CharField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'})
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'middle_name',
            'email', 'phone_number', 'password1', 'password2',)


class StaffRegistrationForm(StudentRegistrationForm):
    STATUS_CHOICE = (
        (True,'Yes'),
        (False, 'No'),
        (None, '---Select yes or No---')
    )
    is_lecturer = forms.BooleanField(
        label='Are you lecturer?',
        widget=forms.Select(choices=STATUS_CHOICE),
        initial=None,
        required=True
        )
    is_hod = forms.BooleanField(
        label='Are you HOD?',
        widget=forms.Select(choices=STATUS_CHOICE),
        initial=None,
        required=True
    )

    class Meta(StudentRegistrationForm.Meta):
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'middle_name','email', 'phone_number',
            'password1', 'password2','is_lecturer',
            'is_hod'
            )