from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.urls import reverse
from lecturer.models import Lecturer
from .models import Course, LecturerCourseAssignment
from .forms import (
    CourseForm,
    LecturerCourseAssignmentForm
    )
from notification.models import Notification
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
from notification.custom import (
    course_assignment_notification,
    course_deassignment_notification
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
        return reverse('department:course-list')


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


class AssignCourseView(View):
    ''' View to assign course to leturers. '''
    form_class = LecturerCourseAssignmentForm
    template_name = 'course/assign_course_form.html'

    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        form = self.form_class(initial={'course':course})
        return render(
            request,
            self.template_name,
            {'form':form, 'course':course}
        )

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            course_assignment_notification(
                sender=request.user,
                target_receiver=form.cleaned_data.get('lecturer').user,
                course=get_object_or_404(Course, id=pk)
            )
            return redirect(
                'department:detail',
                pk=get_object_or_404(Course, id=pk).department.id
            )
        else:
            return render(
                request,
                self.template_name,
                {
                    'form':form,
                    'course':get_object_or_404(Course, id=pk)
                }
            )

class CourseAssignmentDeleteView(DeleteView):
    ''' View to un-assign courses to lecturers.'''
    model = LecturerCourseAssignment
    template_name = 'course/course_assign_confirm_delete.html'
    context_object_name = 'assigned'

    def get_success_url(self):

        course_deassignment_notification(
                sender=self.request.user,
                target_receiver=self.get_object().lecturer.user,
                course=self.get_object().course
        )
        return reverse(
            'department:detail',
            kwargs={'pk':self.get_object().course.department.id}
        )


class CourseAssignmentUpdateView(UpdateView):
    ''' View to update courses assign to lecturers.'''
    model = LecturerCourseAssignment
    fields = (
        'lecturer',
        'is_joined',
    )
    template_name = 'course/course_assign_update.html'
    context_object_name = 'assigned_course'

    def get_success_url(self):
        return reverse(
            'department:detail',
            kwargs={'pk':self.get_object().course.department.id}
        )
