from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Department
from lecturer.models import Lecturer
from course.models import Course
from student.models import Student
from program.models import Program


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/department_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['lecturers'] = Lecturer.objects.all()
        context['courses']    = Course.objects.all()
        return context
    
    