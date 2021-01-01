from django.shortcuts import render, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Department
from lecturer.models import Lecturer
from course.models import (
    Course,
    LecturerCourseAssignment
)
from student.models import Student
from program.models import Program


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/department_detail.html'

    def get_context_data(self, *args, **kwargs):
        department_id = self.kwargs.get('pk')
        context = super().get_context_data(*args, **kwargs)
        try:
            context['lecturers'] = Lecturer.objects.filter(
                            department_id=department_id
                        )
            context['courses']   = Course.objects.filter(
                            department_id=department_id
                        )
            context['assigned_courses']   = LecturerCourseAssignment.objects.all()
        except Lecturer.DoesNotExist:
            context['lecturers'] = None
        except Course.DoesNotExist:
            context['course'] = None

        return context
