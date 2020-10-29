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
        'create_profile/',
        views.StudentCreateView.as_view(),
        name='student-profile'
    )
]