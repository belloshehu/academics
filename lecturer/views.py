from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import (
    CreateView, 
    DeleteView, 
    UpdateView
) 
from django.views.generic import ListView, DetailView
from .models import Lecturer
from users.models import User
from .forms import LecturerForm

class LecturerCreateView(CreateView):
    model = Lecturer
    fields = (
        'department',
        'option',
        'office',
        'gender',
        'photo'
    )
    success_url = 'student:home'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_staff = True
        return redirect(self.success_url)


class LecturerListView(ListView):
    model = Lecturer
    context_object_name = 'lecturers'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        users = User.objects.all()
        context['users'] = [user for user in users if user.is_staff]
        return context


class LecturerDetailView(DetailView):
    model = Lecturer
    template_name = 'lecturer/lecturer_detail.html'


class LecturerUpdateView(UpdateView):
    model = Lecturer
    form_class = LecturerForm
    template_name = 'lecturer/lecturer_update.html'
    fields = (
        'department',
        'option',
        'office',
        'gender',
        'photo'
    )
    def form_valid(self, form, *args, **kwargs):
        form.save()
        print('valid')
        return super().form_valid(form, *args, **kwargs)

    def get_success_url(self): 
        object_id = self.kwargs.get('pk')
        return reverse('lecturer:lecturer-detail', kwargs={'pk':object_id})