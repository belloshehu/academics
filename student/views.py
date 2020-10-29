from django.shortcuts import (
    render, 
    redirect, 
    reverse, 
    get_object_or_404
)
from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView,
    FormView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from department.models import Department
from .models import Student
from .forms import StudentForm


class HomeView(ListView):
    model = Department
    template_name = 'home.html'
    context_object_name = 'departments'
    

class StudentCreateView(LoginRequiredMixin, CreateView):
    ''' View to create Student profile. '''
    model = Student
    '''
    fields = (
            'home_address',
            'phone_number', 
            'department', 
            'program', 
            'option',
            'level',
            'gender',
            'phone_number',
            'photo',
            'year_of_admission',
            'year_of_graduation'
        )
    '''
    form_class = StudentForm
    success_url = 'student:home'

    def form_valid(self, form):
        print('valid')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print('invalid')
        print(self.request.POST.keys())
        return super().form_invalid(form)


class StudentUpdateView(UpdateView):
    ''' Update student instance. '''
    model = Student
    form_class = StudentForm
    template_name = 'student/student_update.html'

    def get_success_url(self):
        return reverse('users:user-profile')

    def get_object(self):
        user_id = self.request.user.id
        return get_object_or_404(Student, user_id=user_id)