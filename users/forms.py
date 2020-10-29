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
            'email', 'password1', 'password2',)


class StaffRegistrationForm(StudentRegistrationForm):
    is_teacher = forms.BooleanField(
        label='',
        widget=forms.CheckboxInput()
        )
    is_hod = forms.BooleanField(
        label='',
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = User
        fields = '__all__'