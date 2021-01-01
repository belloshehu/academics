from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404
)
from custom.views import (
    get_list_or_none,
    filter_list_or_none
)
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View, ListView
from .models import User
from .forms import (
    StudentRegistrationForm,
    LoginForm,
    StaffRegistrationForm
)
from lecturer.models import Lecturer
from student.models import Student
from department.models import Department
from course.models import Course, LecturerCourseAssignment
from notification.models import Notification, IndividualNotification


class HomeView(ListView):
    ''' View for landing page.'''
    model = Department
    template_name = 'home.html'
    context_object_name = 'departments'


class UserCreateView(CreateView):
    ''' View for users sign up.'''
    model = User
    form_class = StudentRegistrationForm
    success_url = 'student:home'


class StudentUserCreateView(CreateView):
    ''' View to register student User. '''
    model = User
    form_class = StudentRegistrationForm
    template_name = 'users/student_registration.html'

    def form_valid(self, form):
        form.instance.is_student = True
        form.instance.is_lecturer = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:signup-success')


class StaffUserCreateView(CreateView):
    ''' View to register student User. '''
    model = User
    form_class = StaffRegistrationForm
    template_name = 'users/staff_registration.html'

    def get_success_url(self):
        return reverse('users:signup-success')

    def form_valid(self, form):
        form.instance.is_student = False
        form.instance.is_staff = True
        return super().form_valid(form)

class RegistrationSuccessView(View):
    ''' View for successful signup. '''
    template_name = 'users/signup_success.html'
    def get(self, request):
        return render(request, self.template_name)


class UserLoginView(View):
    ''' View for logging in users.'''
    template_name = 'users/login_form.html'

    def get(self, request):
        form = LoginForm
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        password = request.POST['password']
        username = request.POST['username']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('student:home'))
        form = LoginForm(request.POST)
        messages.info(request,'Either email or password is not correct.')
        return render(request, self.template_name, {'form':form})


class UserLogoutView(View):

    def get(self, request):
        auth.logout(request)
        return redirect('student:home')


class UserAcademicProfileUpdateView(LoginRequiredMixin, View):
    ''' View to update users academic profile. '''
    def get_user_id(self):
        ''' Returns id a user.'''
        user = get_object_or_404(User, id=self.request.user.id)
        return int(user.id)

    def get(self, request):
        ''' Redirect the request to either
            lecturer or student update views based on the user.
        '''
        if self.request.user.is_staff:
            return redirect(
                'lecturer:lecturer-update',
                pk=self.get_user_id()
            )
        else:
            return redirect(
                'student:student-update',
                pk=self.get_user_id()
            )


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/users_update.html'
    fields = (
        'first_name',
        'last_name',
        'middle_name',
        'phone_number',
        'is_lecturer',
        'is_hod',
    )

    def get_object(self):
        user_id = self.request.user.id
        return get_object_or_404(User, id=user_id)


    def get_success_url(self):
        return reverse('users:user-profile')


class UserProfileView(LoginRequiredMixin,View):
    ''' View to show both personal and academic profiles
        for lecturers and students.
    '''
    template_name = 'users/profile.html'
    def get(self, request):
        obj = None
        courses_assigned = None
        notifications = None
        individual_notifications = None
        if request.user.is_lecturer:
            try:
                obj = get_object_or_404(Lecturer, user_id=request.user.id)
                courses_assigned = LecturerCourseAssignment.objects.filter(
                    lecturer__user_id = request.user.id
                    #lecturer_id=get_object_or_404(Lecturer, user_id=request.user.id)
                )
                notifications = get_list_or_404(
                    Notification,
                    #sender=request.user.id,
                    target_receiver='4'
                    )
                individual_notifications = IndividualNotification.objects.filter (
                    target_receiver_id=request.user.id
                    )
            except:
                pass
        else:
            try:
                courses_assigned = get_list_or_404(Course)
                notifications = get_list_or_404(
                    Notification,
                    sender=request.user.id,
                    target_receiver='2'
                )
                obj = get_object_or_404(
                    Student, user_id=request.user.id
                    )
            except:
                pass
        context = {
            'academic': obj,
            'courses':courses_assigned,
            'notifications':notifications,
            'individual_notifications':individual_notifications
        }
        return render(request, self.template_name, context)


class RegistrationMenuView(View):
    ''' View to present sign up menu. '''
    template_name = 'users/registration_menu.html'

    def get(self, request):
        return render(request, self.template_name)
