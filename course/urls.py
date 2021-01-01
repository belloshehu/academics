from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path(
        'list/',
        views.CourseListView.as_view(),
        name='course-list'
    ),
    path(
        'detail/<int:pk>/',
        views.CourseDetailView.as_view(),
        name='course-detail'
    ),
    path(
        'update/<int:pk>/',
        views.CourseUpdateView.as_view(),
        name='course-update'
    ),
    path(
        'delete/<int:pk>/',
        views.CourseDeleteView.as_view(),
        name='course-delete'
    ),
    path(
        'create/',
        views.CourseCreateView.as_view(),
        name='course-create'
    ),
    path(
        'assign/<int:pk>/',
        views.AssignCourseView.as_view(),
        name='course-assign'
    ),
    path(
        'assign_delete/<int:pk>/',
        views.CourseAssignmentDeleteView.as_view(),
        name='course-assign-delete'
    ),
    path(
        'assign_update/<int:pk>/',
        views.CourseAssignmentUpdateView.as_view(),
        name='course-assign-update'
    )
]