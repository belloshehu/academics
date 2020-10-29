from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Course
from .forms import CourseForm
from django.views.generic.edit import (
    UpdateView, 
    DeleteView
)
from django.views.generic import (
    CreateView,
    ListView,
    DetailView, 
    View
)


class CourseListView(ListView):
    ''' View to list courses '''
    model         = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    ''' View to present detail of a Course.'''
    model         = Course
    template_name = 'course/course_detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course:course-list')    


class CourseUpdateView(UpdateView):
    ''' View to update instance of Course.'''
    model         = Course
    form_class    = CourseForm
    template_name = 'course/course_update.html'

    def get_success_url(self):
        object_id = self.kwargs.get('pk')
        return reverse('course:course-detail', kwargs={'pk':object_id})

    def get_context_data(self, *args, **kwargs):
        context  = super().get_context_data(*args, **kwargs)
        obj_id = self.kwargs.get('pk')
        context['course'] = get_object_or_404(Course, id=obj_id)
        return context

class CourseDeleteView(DeleteView):
    ''' View to delete instance of Course. '''
    model = Course
    template_name = 'course/course_delete_confirm.html'
