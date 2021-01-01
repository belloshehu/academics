from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path(
        'home/',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'create/',
        views.StudentCreateView.as_view(),
        name='student-create'
    ),
    path(
        'update/<int:pk>/',
        views.StudentUpdateView.as_view(),
        name='student-update'
    )
]