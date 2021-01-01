from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView
)
from django.views.generic import ListView, DetailView
from .models import Lecturer
from users.models import User
from .forms import LecturerForm

class LecturerCreateView(LoginRequiredMixin, CreateView):
    model = Lecturer
    template_name = 'lecturer/lecturer_form.html'
    #form_class = LecturerForm
    fields = (
        'department',
        'option',
        'office',
        'gender',
        'photo',
        'is_serving'
    )
    def form_invalid(self, form):
        print(self.request.POST)
        print('invslid')
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:user-profile')


class LecturerListView(ListView):
    model = Lecturer
    context_object_name = 'lecturers'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        users = User.objects.all()
        context['users'] = [user for user in users if user.is_lecturer]
        return context


class LecturerDetailView(DetailView):
    model = Lecturer
    template_name = 'lecturer/lecturer_detail.html'


class LecturerUpdateView(UpdateView):
    ''' View to update lecturer academic profile. '''
    model = Lecturer
    template_name = 'lecturer/lecturer_update.html'
    fields = (
        'department',
        'option',
        'office',
        'gender',
        'photo'
    )

    def get_success_url(self):
        return reverse('users:user-profile')