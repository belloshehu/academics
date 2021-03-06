from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'register/',
        views.UserCreateView.as_view(),
        name='register'
    ),
    path(
        'login/',
        views.UserLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.UserLogoutView.as_view(),
        name='logout'
    ),
    path(
        'update/',
        views.UserUpdateView.as_view(),
        name='users-update'
    ),
    path(
        'profile/',
        views.UserProfileView.as_view(),
        name='user-profile'
    ),
    path(
        'academic/',
        views.UserAcademicProfileUpdateView.as_view(),
        name='academic-update'
    ),
    path(
        'registration-menu/',
        views.RegistrationMenuView.as_view(),
        name='registration-menu'
    ),
    path(
        'student-registration/',
        views.StudentUserCreateView.as_view(),
        name='student-registration'
    ),
    path(
        'staff-registration/',
        views.StaffUserCreateView.as_view(),
        name='staff-registration'
    ),
    path(
        'signup-success/',
        views.RegistrationSuccessView.as_view(),
        name='signup-success'
    )
]