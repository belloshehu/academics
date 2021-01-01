from django.urls import path
from . import views

app_name = 'lecturer'
urlpatterns = [
    path(
        'create/',
        views.LecturerCreateView.as_view(),
        name='lecturer-create'
    ),
    path(
        'list/',
        views.LecturerListView.as_view(),
        name='lecturer-list'
    ),
    path(
        'detail/<int:pk>/',
        views.LecturerDetailView.as_view(),
        name='lecturer-detail'
    ),
    path(
        'update/<int:pk>/',
        views.LecturerUpdateView.as_view(),
        name='lecturer-update'
    )
]